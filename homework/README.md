# Task: Building a Fantasy Character Generator
Your goal is to create an AI agent that generates fantasy character(called `NPC` from now on) based on the text descriptions. 

You can use any prompting technique learned in the theoretical part, mix them etc.

You're also encouraged to think out of the box and just try each approach you can think of!

## What You'll Build
An AI-powered NPC generator that takes a text prompt (_e.g., "Create a mysterious elven ranger who guards the ancient woods and speaks in riddles"_) and returns a complete [NPC object](./models.py) with:
- Name
- Class (Warrior, Mage, Rogue, etc.)
- Hostility status
- Catchphrase
- Stats (strength, charisma, intelligence)

## Your Tasks
Replace the [placeholder agent implementation](./agent.py). Your solution can(and most probably should):
- Use one of the prompt techniques we've discussed
- Test how often it fails, play with retries param
- Run your agent with `task run`* command to see it in action
- When ready, run the tests with `task test`** command!
- At the end, we'll have a brief discussion about your solutions

## Tips
- Try to be as specific as possible
- You can modify anything to your own liking! (with small exception - do not modify main function signature in `agent.py`)
- The tests will validate the output against model schema, and test stats field

## Need Help? 

### Ask me anything! 

### ...or:
- Review the [`models.py`](./models.py) file for the complete NPC schema
- Check the existing workshop examples in the main notebook
- Test with simple prompts first, then add complexity

Good luck!

<br><br>

*or if you don't have [Task/Taskfile](https://taskfile.dev/docs/installation), run: `docker compose exec jupyter python -m homework.agent`

**or if you don't have [Task/Taskfile](https://taskfile.dev/docs/installation), run: `docker compose exec jupyter pytest homework_test/agent_test.py --log-cli-level=INFO`