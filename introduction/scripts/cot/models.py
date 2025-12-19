from pydantic import BaseModel, Field


class PlainAnswer(BaseModel):
    answer: int = Field(description="Answer to the question")


class CoTAnswer(BaseModel):
    thinking: str = Field(
        description=(
            "First, break down the user's question to identify the core task. "
            "Second, outline the sequential steps required to solve the task. "
            "Third, execute each step, showing your reasoning and any calculations involved. "
            "The thinking process should logically lead to the final answer."
        )
    )
    answer: int = Field(
        description="The final numerical answer derived from the step-by-step thinking process."
    )
