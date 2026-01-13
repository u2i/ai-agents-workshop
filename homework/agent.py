import os
import asyncio
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider
from pydantic_ai import Agent

from homework.models import NPC

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434/v1")
MODEL = "qwen2.5:1.5b"

ollama_model = OpenAIChatModel(
    model_name=MODEL,
    provider=OllamaProvider(base_url=OLLAMA_BASE_URL),
)

system_prompt = """
This is a placeholder for your prompt...
"""

# You may also modify this agent...
agent = Agent(ollama_model, system_prompt=system_prompt, retries=5)


async def main(
    user_prompt: str = "Create a mysterious elven ranger who guards the ancient woods and speaks in riddles.",
) -> NPC:
    raise NotImplementedError


if __name__ == "__main__":
    npc = asyncio.run(main())
