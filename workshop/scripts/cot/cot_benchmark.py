from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from models import CoTAnswer, PlainAnswer
import asyncio

OLLAMA_BASE_URL = "http://localhost:11434/v1"
MODEL = "qwen2.5:1.5b"
ollama_model = OpenAIChatModel(
    model_name=MODEL,
    provider=OllamaProvider(base_url=OLLAMA_BASE_URL),
)

plain_answer_agent = Agent(ollama_model, output_type=PlainAnswer, retries=9)
cot_agent = Agent(ollama_model, output_type=CoTAnswer, retries=9)


async def run_benchmark(prompt: str, correct_answer: int, iterations: int):
    just_answer_correct = 0
    cot_correct = 0

    just_answer_correct = await _run_benchmark(
        "PlainAnswer", plain_answer_agent, prompt, correct_answer, iterations
    )
    cot_correct = await _run_benchmark(
        "CoT", cot_agent, prompt, correct_answer, iterations
    )

    data = {
        "Method": ["PlainAnswer", "CoT"],
        "Correct": [just_answer_correct, cot_correct],
        "Incorrect": [iterations - just_answer_correct, iterations - cot_correct],
    }
    df = pd.DataFrame(data)
    df_melted = df.melt(id_vars="Method", var_name="Result", value_name="Count")

    plt.figure(figsize=(8, 6))
    sns.barplot(data=df_melted, x="Method", y="Count", hue="Result")
    plt.title("Benchmark: PlainAnswer vs. Chain of Thought")
    plt.ylabel("Number of Responses")
    plt.show()


async def _run_benchmark(
    benchmark_name: str, agent: Agent, prompt: str, correct_answer: int, iterations: int
):
    correct = 0
    print(f"\nRunning '{benchmark_name}' benchmark...")
    for i in range(iterations):
        print(f"Iteration {i+1}/{iterations}", end="\r")
        try:
            result = await agent.run(prompt)
            if result.output.answer == correct_answer:
                correct += 1
        except Exception as e:
            print(f"An error occurred in {benchmark_name} iteration {i+1}: {e}")

    print(
        f"{benchmark_name} correct: {correct}/{iterations} ({(correct/iterations)*100:.2f}%)",
        end="\n\n",
    )
    return correct


if __name__ == "__main__":
    asyncio.run(
        run_benchmark(
            prompt="How many times does the letter 'r' appear in the word 'strawberry'?",
            correct_answer=3,
            iterations=60,
        )
    )
