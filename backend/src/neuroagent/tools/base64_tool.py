"""Base64 encoder/decoder tool."""

import base64
import logging
from typing import ClassVar

from pydantic import BaseModel, Field

from neuroagent.tools.base_tool import BaseMetadata, BaseTool

logger = logging.getLogger(__name__)


class Base64Input(BaseModel):
    """Input schema for Base64 tool."""

    text: str = Field(description="Text to encode or decode")
    operation: str = Field(default="encode", description="Operation: encode or decode")


class Base64Metadata(BaseMetadata):
    """Metadata for Base64 tool."""

    pass


class Base64ToolOutput(BaseModel):
    """Output of the base64 tool."""

    result: str
    operation: str


class Base64Tool(BaseTool):
    """Tool that encodes/decodes base64."""

    name: ClassVar[str] = "base64-tool"
    name_frontend: ClassVar[str] = "Base64 Encoder/Decoder"
    utterances: ClassVar[list[str]] = [
        "Encode to base64",
        "Decode base64",
        "Base64 conversion",
    ]
    description: ClassVar[str] = "Encodes text to base64 or decodes base64 to text"
    description_frontend: ClassVar[str] = """Encode and decode base64 strings:
    • Encode text to base64 format
    • Decode base64 back to text
    • Handles UTF-8 text encoding
    
    Useful for data encoding and web development."""
    metadata: Base64Metadata
    input_schema: Base64Input

    async def arun(self) -> Base64ToolOutput:
        """Encode or decode base64."""
        if self.input_schema.operation == "encode":
            result = base64.b64encode(self.input_schema.text.encode()).decode()
        elif self.input_schema.operation == "decode":
            result = base64.b64decode(self.input_schema.text).decode()
        else:
            raise ValueError("operation must be 'encode' or 'decode'")

        return Base64ToolOutput(result=result, operation=self.input_schema.operation)

    @classmethod
    async def is_online(cls) -> bool:
        """Check if the tool is online."""
        return True