"""QR code data generator tool."""

import logging
from typing import ClassVar

from pydantic import BaseModel, Field

from neuroagent.tools.base_tool import BaseMetadata, BaseTool

logger = logging.getLogger(__name__)


class QrCodeInput(BaseModel):
    """Input schema for QR Code tool."""

    data: str = Field(description="Data to encode in QR code")
    size: str = Field(default="medium", description="QR code size: small, medium, large")


class QrCodeMetadata(BaseMetadata):
    """Metadata for QR Code tool."""

    pass


class QrCodeToolOutput(BaseModel):
    """Output of the QR code tool."""

    data: str
    qr_url: str
    size: str


class QrCodeTool(BaseTool):
    """Tool that generates QR code URLs."""

    name: ClassVar[str] = "qr-code-tool"
    name_frontend: ClassVar[str] = "QR Code Generator"
    utterances: ClassVar[list[str]] = [
        "Generate QR code",
        "Create QR code for this",
        "Make QR code",
    ]
    description: ClassVar[str] = "Generates QR code URLs using Google Charts API format"
    description_frontend: ClassVar[str] = """Generate QR codes for any data:
    • Text, URLs, contact info
    • Multiple size options
    • Returns Google Charts API URL
    
    Perfect for sharing links, contact details, or any text data."""
    metadata: QrCodeMetadata
    input_schema: QrCodeInput

    async def arun(self) -> QrCodeToolOutput:
        """Generate QR code URL."""
        size_map = {"small": "150x150", "medium": "200x200", "large": "300x300"}
        qr_size = size_map.get(self.input_schema.size, "200x200")
        
        # URL encode the data
        encoded_data = self.input_schema.data.replace(" ", "%20").replace("&", "%26")
        qr_url = f"https://chart.googleapis.com/chart?chs={qr_size}&cht=qr&chl={encoded_data}"

        return QrCodeToolOutput(
            data=self.input_schema.data,
            qr_url=qr_url,
            size=self.input_schema.size,
        )

    @classmethod
    async def is_online(cls) -> bool:
        """Check if the tool is online."""
        return True