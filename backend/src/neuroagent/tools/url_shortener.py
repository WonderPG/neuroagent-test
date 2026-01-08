"""URL shortener simulator tool."""

import logging
import random
import string
from typing import ClassVar

from pydantic import BaseModel, Field

from neuroagent.tools.base_tool import BaseMetadata, BaseTool

logger = logging.getLogger(__name__)


class UrlShortenerInput(BaseModel):
    """Input schema for URL Shortener tool."""

    url: str = Field(description="URL to shorten")
    custom_code: str = Field(default="", description="Custom short code (optional)")


class UrlShortenerMetadata(BaseMetadata):
    """Metadata for URL Shortener tool."""

    pass


class UrlShortenerToolOutput(BaseModel):
    """Output of the URL shortener tool."""

    original_url: str
    short_url: str
    short_code: str


class UrlShortenerTool(BaseTool):
    """Tool that simulates URL shortening."""

    name: ClassVar[str] = "url-shortener-tool"
    name_frontend: ClassVar[str] = "URL Shortener"
    utterances: ClassVar[list[str]] = [
        "Shorten this URL",
        "Create short link",
        "Generate short URL",
    ]
    description: ClassVar[str] = "Simulates URL shortening by generating short codes"
    description_frontend: ClassVar[str] = """Simulate URL shortening service:
    • Generate random short codes
    • Custom short codes supported
    • Creates short.ly/[code] format URLs
    
    Note: This is a simulation tool for testing purposes."""
    metadata: UrlShortenerMetadata
    input_schema: UrlShortenerInput

    async def arun(self) -> UrlShortenerToolOutput:
        """Generate shortened URL."""
        if self.input_schema.custom_code:
            short_code = self.input_schema.custom_code
        else:
            short_code = "".join(random.choices(string.ascii_letters + string.digits, k=6))
        
        short_url = f"https://short.ly/{short_code}"

        return UrlShortenerToolOutput(
            original_url=self.input_schema.url,
            short_url=short_url,
            short_code=short_code,
        )

    @classmethod
    async def is_online(cls) -> bool:
        """Check if the tool is online."""
        return True