from typing import Literal
from pydantic import BaseModel, Field


class SentimentAnalysis(BaseModel):
    sentiment: Literal["Positive", "Negative", "Neutral"] = Field(
        description="The sentiment of the text."
    )
