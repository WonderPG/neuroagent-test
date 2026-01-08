"""Hash generator tool."""

import hashlib
import logging
from typing import ClassVar

from pydantic import BaseModel, Field

from neuroagent.tools.base_tool import BaseMetadata, BaseTool

logger = logging.getLogger(__name__)


class HashInput(BaseModel):
    """Input schema for Hash tool."""

    text: str = Field(description="Text to hash")
    algorithm: str = Field(default="sha256", description="Hash algorithm: md5, sha1, sha256")


class HashMetadata(BaseMetadata):
    """Metadata for Hash tool."""

    pass


class HashToolOutput(BaseModel):
    """Output of the hash tool."""

    hash_value: str
    algorithm: str


class HashTool(BaseTool):
    """Tool that generates hashes."""

    name: ClassVar[str] = "hash-tool"
    name_frontend: ClassVar[str] = "Hash Generator"
    utterances: ClassVar[list[str]] = [
        "Generate hash",
        "Hash this text",
        "Create checksum",
    ]
    description: ClassVar[str] = "Generates cryptographic hashes using MD5, SHA1, or SHA256"
    description_frontend: ClassVar[str] = """Generate cryptographic hashes:
    • MD5 hashes (32 characters)
    • SHA1 hashes (40 characters)  
    • SHA256 hashes (64 characters)
    
    Perfect for checksums, data integrity, and security applications."""
    metadata: HashMetadata
    input_schema: HashInput

    async def arun(self) -> HashToolOutput:
        """Generate hash."""
        text_bytes = self.input_schema.text.encode()
        
        if self.input_schema.algorithm == "md5":
            hash_value = hashlib.md5(text_bytes).hexdigest()
        elif self.input_schema.algorithm == "sha1":
            hash_value = hashlib.sha1(text_bytes).hexdigest()
        elif self.input_schema.algorithm == "sha256":
            hash_value = hashlib.sha256(text_bytes).hexdigest()
        else:
            raise ValueError("algorithm must be md5, sha1, or sha256")

        return HashToolOutput(hash_value=hash_value, algorithm=self.input_schema.algorithm)

    @classmethod
    async def is_online(cls) -> bool:
        """Check if the tool is online."""
        return True