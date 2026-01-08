"""Coin flip tool."""

import logging
import random
from typing import ClassVar

from pydantic import BaseModel, Field

from neuroagent.tools.base_tool import BaseMetadata, BaseTool

logger = logging.getLogger(__name__)


class CoinFlipInput(BaseModel):
    """Input schema for Coin Flip tool."""

    flips: int = Field(default=1, description="Number of coin flips")


class CoinFlipMetadata(BaseMetadata):
    """Metadata for Coin Flip tool."""

    pass


class CoinFlipToolOutput(BaseModel):
    """Output of the coin flip tool."""

    results: list[str]
    heads_count: int
    tails_count: int


class CoinFlipTool(BaseTool):
    """Tool that flips coins."""

    name: ClassVar[str] = "coin-flip-tool"
    name_frontend: ClassVar[str] = "Coin Flip"
    utterances: ClassVar[list[str]] = [
        "Flip a coin",
        "Heads or tails",
        "Coin toss",
    ]
    description: ClassVar[str] = "Flips coins and returns heads or tails results"
    description_frontend: ClassVar[str] = """Flip coins for random decisions:
    • Single or multiple flips
    • Returns heads/tails results
    • Shows count summary
    
    Perfect for making binary decisions or probability experiments."""
    metadata: CoinFlipMetadata
    input_schema: CoinFlipInput

    async def arun(self) -> CoinFlipToolOutput:
        """Flip coins."""
        if self.input_schema.flips < 1 or self.input_schema.flips > 100:
            raise ValueError("flips must be between 1 and 100")

        results = [random.choice(["heads", "tails"]) for _ in range(self.input_schema.flips)]
        heads_count = results.count("heads")
        tails_count = results.count("tails")

        return CoinFlipToolOutput(
            results=results,
            heads_count=heads_count,
            tails_count=tails_count,
        )

    @classmethod
    async def is_online(cls) -> bool:
        """Check if the tool is online."""
        return True