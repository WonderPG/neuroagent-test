"""Calculator tool."""

import logging
from typing import ClassVar

from pydantic import BaseModel, Field

from neuroagent.tools.base_tool import BaseMetadata, BaseTool

logger = logging.getLogger(__name__)


class CalculatorInput(BaseModel):
    """Input schema for Calculator tool."""

    expression: str = Field(description="Mathematical expression to evaluate")


class CalculatorMetadata(BaseMetadata):
    """Metadata for Calculator tool."""

    pass


class CalculatorToolOutput(BaseModel):
    """Output of the calculator tool."""

    result: float
    expression: str


class CalculatorTool(BaseTool):
    """Tool that evaluates mathematical expressions."""

    name: ClassVar[str] = "calculator-tool"
    name_frontend: ClassVar[str] = "Calculator"
    utterances: ClassVar[list[str]] = [
        "Calculate this",
        "What is 2 + 2?",
        "Solve math problem",
    ]
    description: ClassVar[str] = "Evaluates basic mathematical expressions"
    description_frontend: ClassVar[str] = """Perform mathematical calculations:
    • Basic arithmetic (+, -, *, /)
    • Mathematical functions (sqrt, sin, cos, etc.)
    • Supports parentheses and order of operations"""
    metadata: CalculatorMetadata
    input_schema: CalculatorInput

    async def arun(self) -> CalculatorToolOutput:
        """Evaluate mathematical expression."""
        import math
        
        allowed = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed.update({"abs": abs, "round": round})
        
        try:
            result = eval(self.input_schema.expression, {"__builtins__": {}}, allowed)
            return CalculatorToolOutput(result=float(result), expression=self.input_schema.expression)
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}") from e

    @classmethod
    async def is_online(cls) -> bool:
        """Check if the tool is online."""
        return True