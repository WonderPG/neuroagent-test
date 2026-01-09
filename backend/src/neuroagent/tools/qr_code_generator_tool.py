"""QR Code Generator Tool for creating QR codes from text, URLs, or data identifiers."""

from typing import Dict, Any
import qrcode
import io
import base64
from pydantic import BaseModel, Field
from neuroagent.tools.base_tool import BaseTool


class QRCodeInput(BaseModel):
    """Input schema for QR code generation."""
    data: str = Field(description="Text, URL, or data to encode in QR code")
    size: int = Field(default=10, description="Size of QR code (1-40)")
    border: int = Field(default=4, description="Border size around QR code")


class QRCodeGeneratorTool(BaseTool):
    """Tool for generating QR codes from text or URLs."""
    
    name: str = "qr_code_generator"
    description: str = "Generate QR codes from text, URLs, or data identifiers"
    args_schema = QRCodeInput
    
    def _run(self, data: str, size: int = 10, border: int = 4) -> Dict[str, Any]:
        """Generate QR code from input data."""
        
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=size,
                border=border,
            )
            qr.add_data(data)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Convert to base64 for display
            buffer = io.BytesIO()
            img.save(buffer, format='PNG')
            img_str = base64.b64encode(buffer.getvalue()).decode()
            
            return {
                "success": True,
                "data_encoded": data,
                "qr_code_base64": img_str,
                "size": size,
                "border": border,
                "format": "PNG"
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "data_attempted": data
            }