def get_plain_system_prompt() -> str:
    return "You are a sentiment analysis expert specializing in software user feedback. Analyze the sentiment of the text."


def get_few_shot_system_prompt() -> str:
    few_shot_system_prompt = f"""
    You are a sentiment analysis expert specializing in software user feedback.
    
    ### Examples:
    """

    EXAMPLES = [
        # Sarcasm - sounds positive but is clearly negative
        (
            "I love how the app freezes every time I try to export. Really keeps me on my toes!",
            "Negative",
        ),
        # Bug report with delightful language - still a bug = negative
        (
            "There's a charming little bug where my profile picture rotates 360 degrees when clicked. Hilarious, but not sure it's intentional.",
            "Negative",
        ),
        # Frustrated question - implies missing feature
        (
            "Is there really no way to undo changes? Am I missing something obvious here?",
            "Negative",
        ),
        # Feature request with positive language
        (
            "Adding keyboard shortcuts would be a game-changer for power users like me!",
            "Positive",
        ),
        # Positive feedback disguised as a complaint
        (
            "My only issue is that this tool works so well, I can't justify using anything else. Great work!",
            "Positive",
        ),
        # Neutral technical observation
        ("Memory consumption increased by 12% after the last update.", "Neutral"),
        # Technical feature request - neutral statement
        ("The API should support pagination for large result sets.", "Neutral"),
        # Comparative negative - implies current version is worse
        (
            "The export feature used to be instant, but now it takes several seconds.",
            "Negative",
        ),
    ]

    for text, sentiment in EXAMPLES:
        few_shot_system_prompt += (
            f'User text: "{text}"\nResponse: {{"sentiment": "{sentiment}"}}\n'
        )

    return few_shot_system_prompt
