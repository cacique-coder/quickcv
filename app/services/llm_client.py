import asyncio
import logging
import os
import subprocess
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


# Pricing per million tokens (USD) — update when model changes
MODEL_PRICING = {
    "claude-sonnet-4-20250514": {"input": 3.00, "output": 15.00},
    "claude-sonnet-4-20250514:thinking": {"input": 3.00, "output": 15.00},
    "claude-haiku-4-5-20251001": {"input": 0.80, "output": 4.00},
    "claude-opus-4-6": {"input": 15.00, "output": 75.00},
}


@dataclass
class LLMResult:
    """Response from an LLM call, with optional usage/cost metadata."""
    text: str
    model: str = ""
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float = 0.0
    cache_read_tokens: int = 0
    cache_creation_tokens: int = 0


def _estimate_cost(model: str, input_tokens: int, output_tokens: int) -> float:
    pricing = MODEL_PRICING.get(model)
    if not pricing:
        return 0.0
    return (input_tokens * pricing["input"] + output_tokens * pricing["output"]) / 1_000_000


class LLMClient(ABC):
    @abstractmethod
    async def generate(self, prompt: str) -> LLMResult:
        """Send a prompt and return the response with usage metadata."""


class AnthropicAPIClient(LLMClient):
    def __init__(self, model: str = "claude-sonnet-4-20250514"):
        import anthropic

        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable is required")
        self.client = anthropic.AsyncAnthropic(api_key=api_key)
        self.model = model

    async def generate(self, prompt: str) -> LLMResult:
        # Split on the first delimiter to extract system vs user content.
        split_marker = "===BEGIN CANDIDATE CV"
        if split_marker in prompt:
            idx = prompt.index(split_marker)
            system_text = prompt[:idx].strip()
            user_text = prompt[idx:].strip()
        else:
            system_text = ""
            user_text = prompt

        message = await self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=system_text,
            messages=[{"role": "user", "content": user_text}],
        )

        usage = message.usage
        input_tokens = usage.input_tokens
        output_tokens = usage.output_tokens
        cache_read = getattr(usage, "cache_read_input_tokens", 0) or 0
        cache_creation = getattr(usage, "cache_creation_input_tokens", 0) or 0

        return LLMResult(
            text=message.content[0].text,
            model=self.model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cost_usd=round(_estimate_cost(self.model, input_tokens, output_tokens), 6),
            cache_read_tokens=cache_read,
            cache_creation_tokens=cache_creation,
        )


class ClaudeCodeClient(LLMClient):
    def __init__(self, model: str = "sonnet", timeout: int = 120):
        self.model = model
        self.timeout = timeout

    async def generate(self, prompt: str) -> LLMResult:
        # Remove CLAUDECODE env var so the CLI doesn't think it's nested
        env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}

        proc = await asyncio.create_subprocess_exec(
            "claude", "-p", prompt, "--model", self.model,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=env,
        )

        try:
            stdout, stderr = await asyncio.wait_for(
                proc.communicate(), timeout=self.timeout
            )
        except asyncio.TimeoutError:
            proc.kill()
            await proc.communicate()
            raise RuntimeError(f"Claude CLI timed out after {self.timeout}s")

        if proc.returncode != 0:
            raise RuntimeError(f"Claude CLI failed: {stderr.decode()}")

        return LLMResult(
            text=stdout.decode().strip(),
            model=f"claude-code:{self.model}",
        )
