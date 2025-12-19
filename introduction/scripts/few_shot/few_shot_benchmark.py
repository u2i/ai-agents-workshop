import asyncio
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider
from scripts.few_shot.models import SentimentAnalysis
from scripts.few_shot.prompts import get_plain_system_prompt, get_few_shot_system_prompt

OLLAMA_BASE_URL = "http://localhost:11434/v1"
MODEL = "llama3.2"
ollama_model = OpenAIChatModel(
    model_name=MODEL,
    provider=OllamaProvider(base_url=OLLAMA_BASE_URL),
)

plain_answer_agent = Agent(
    ollama_model,
    output_type=SentimentAnalysis,
    system_prompt=get_plain_system_prompt(),
    retries=9,
)

few_shot_agent = Agent(
    ollama_model,
    output_type=SentimentAnalysis,
    system_prompt=get_few_shot_system_prompt(),
    retries=9,
)


TEST_DATA = [
    # Implicitly positive - user found a workaround, but the feature is good
    (
        "It took a bit of digging, but I found the setting to disable automatic updates. This level of control is great.",
        "Positive",
    ),
    # Sarcastic complaint
    (
        "I love how the application logs me out every 15 minutes of inactivity. It's a fantastic security feature that doesn't disrupt my workflow at all.",
        "Negative",
    ),
    # Technical feature request that sounds neutral
    (
        "The API should return a 409 Conflict status code when a duplicate record is created.",
        "Neutral",
    ),
    # Comparative feedback, subtly negative
    (
        "The mobile app is functional, but it lacks the advanced reporting features of the desktop version.",
        "Negative",
    ),
    # Frustration masked as a question
    (
        "Am I missing something, or is there really no way to batch-edit records?",
        "Negative",
    ),
    # Positive feedback disguised as a problem
    (
        "My only complaint is that I can't seem to find a 'buy you a coffee' button in the app. This tool has saved me countless hours.",
        "Positive",
    ),
    # Neutral, but could be misinterpreted as negative
    (
        "The memory usage of the application appears to have increased by 15% in the latest build.",
        "Neutral",
    ),
    # A bug report that sounds like a feature
    (
        "Every time I click the save button, I get a shower of confetti on my screen. It's delightful, but probably not intended.",
        "Negative",
    ),
]


async def run_benchmark(iterations: int):
    plain_answer_task = asyncio.create_task(
        _run_benchmark("PlainAnswer", plain_answer_agent, iterations)
    )
    few_shot_task = asyncio.create_task(
        _run_benchmark("FewShot", few_shot_agent, iterations)
    )

    plain_answer_correct, few_shot_correct = await asyncio.gather(
        plain_answer_task, few_shot_task
    )

    data = {
        "Method": ["PlainAnswer", "FewShot"],
        "Correct": [plain_answer_correct, few_shot_correct],
        "Incorrect": [
            iterations * len(TEST_DATA) - plain_answer_correct,
            iterations * len(TEST_DATA) - few_shot_correct,
        ],
    }
    df = pd.DataFrame(data)
    df_melted = df.melt(id_vars="Method", var_name="Result", value_name="Count")

    plt.figure(figsize=(8, 6))
    sns.barplot(data=df_melted, x="Method", y="Count", hue="Result")
    plt.title("Benchmark: PlainAnswer vs. Few-Shot Prompting")
    plt.ylabel("Number of Responses")
    plt.savefig("static/SentimentAnalysis_PlainAnswer_vs_FewShot.png")
    print(
        "\nBenchmark chart saved to static/SentimentAnalysis_PlainAnswer_vs_FewShot.png"
    )


async def _run_benchmark(benchmark_name: str, agent: Agent, iterations: int):
    correct = 0
    print(f"\nRunning '{benchmark_name}' benchmark...")

    for i in range(iterations):
        for text, correct_sentiment in TEST_DATA:
            prompt = f"Analyze the sentiment of the following text: '{text}'"
            print(f"Iteration {i+1}/{iterations} for '{text}'", end="\r")

            while True:
                try:
                    result = await agent.run(prompt)
                    if result.output.sentiment == correct_sentiment:
                        correct += 1
                    break  # Break the loop on success
                except Exception as e:
                    print(
                        f"\nAn error occurred in {benchmark_name} iteration {i+1} for '{text}'. Retrying..."
                    )

    total_attempts = iterations * len(TEST_DATA)
    print(
        f"{benchmark_name} correct: {correct}/{total_attempts} ({(correct/total_attempts)*100:.2f}%)",
        end="\n\n",
    )
    return correct


if __name__ == "__main__":
    asyncio.run(run_benchmark(iterations=5))
