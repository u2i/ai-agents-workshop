import os
import asyncio
from typing import TypeVar, Any

from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider
from pydantic_ai import Agent, UnexpectedModelBehavior

from homework.models import NPC, CreativeResponse, Stats, Class, StatsResponse

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434/v1")
MODEL = "llama3.2"

ollama_model = OpenAIChatModel(
    model_name=MODEL,
    provider=OllamaProvider(base_url=OLLAMA_BASE_URL),
)

creative_system_prompt = """
You are an expert in creating names, catchphrases and hostility for fantasy RPG NPCs.
Given a user prompt describing the type of NPC to create, you will generate a name,catchphrase and if it's hostile.
"""
statistical_system_prompt = """
You are an expert in generating RPG character statistics. Given a user prompt describing the type of NPC to create, you will generate appropriate strength, charisma, and intelligence stats for that character. Short answer.
Examples:
- Warrior: strength 18, charisma 12, intelligence 8
- Merchant: strength 10, charisma 18, intelligence 14
"""
class_system_prompt = """
You are an expert in classifying fantasy RPG NPCs into their appropriate classes based on user prompts.
"""
# You may also modify this agent...
creative_agent = Agent(ollama_model, system_prompt=creative_system_prompt, output_type=CreativeResponse, retries=3)
statistics_agent = Agent(ollama_model, system_prompt=statistical_system_prompt,output_type=StatsResponse, retries=3)
class_agent = Agent(ollama_model,system_prompt=class_system_prompt , output_type=Class, retries=3)

T = TypeVar("T")
async def run_with_fresh_starts(agent: Agent[Any, T], prompt: str, max_retries: int = 3) -> T:
    last_exception = None
    for _ in range(max_retries):
        try:
            result = await agent.run(prompt)
            return result.output
        except UnexpectedModelBehavior as e:
            last_exception = e
            continue
        except Exception as e:
            last_exception = e
            continue

    raise last_exception or Exception("Agent failed to generate valid response after retries")


async def main(
    user_prompt: str = "Create a mysterious elven ranger who guards the ancient woods and speaks in riddles.",
) :
    creative_task = run_with_fresh_starts(creative_agent, user_prompt)
    class_task = run_with_fresh_starts(class_agent, user_prompt)

    cr_data, chosen_class = await asyncio.gather(creative_task, class_task)
    print(cr_data)
    print(f"Chosen class: {chosen_class}")
    stats_prompt = f"Class: {chosen_class}. Description: {user_prompt}"
    stats_data = await run_with_fresh_starts(statistics_agent,stats_prompt)
    print(stats_data)
    stats = Stats(
        strength=max(1, min(20,stats_data.strength)),
        charisma=max(1, min(20,stats_data.charisma)),
        intelligence=max(1, min(20,stats_data.intelligence)),
    )
    npc = NPC(
        name=cr_data.name,
        npc_class=chosen_class,
        is_hostile=cr_data.is_hostile,
        catchphrase=cr_data.catchphrase,
        stats=stats,
    )
    print(npc)

    return npc

if __name__ == "__main__":
    npc = asyncio.run(main())
