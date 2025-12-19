import pytest
from task.agent import main
from task.models import NPC, Class
from test.helpers import skip_on_error, probabilistic_test


@pytest.mark.asyncio
@skip_on_error
@probabilistic_test(times=3, threshold=0)
async def test_generation_runs_without_errors():
    npc = await main()

    assert npc is not None
    assert isinstance(npc, NPC)
    assert isinstance(npc.name, str)
    assert len(npc.name) > 0
    assert isinstance(npc.npc_class, Class)
    assert isinstance(npc.is_hostile, bool)
    assert isinstance(npc.catchphrase, str)
    assert len(npc.catchphrase) > 0
    assert 1 <= npc.stats.strength <= 20
    assert 1 <= npc.stats.charisma <= 20
    assert 1 <= npc.stats.intelligence <= 20


@pytest.mark.asyncio
@skip_on_error
@probabilistic_test(times=1, threshold=0)
@pytest.mark.parametrize(
    "class_name,user_prompt,expected_stats",
    [
        (
            Class.WARRIOR,
            "Create a brave warrior who excels in combat.",
            {"strength": (15, 20), "charisma": (8, 16), "intelligence": (6, 14)},
        ),
        (
            Class.MAGE,
            "Create a powerful mage skilled in arcane arts.",
            {"strength": (4, 10), "charisma": (10, 20), "intelligence": (15, 20)},
        ),
        (
            Class.MERCHANT,
            "Create a wealthy merchant skilled in persuasion.",
            {"strength": (5, 12), "charisma": (14, 20), "intelligence": (12, 18)},
        ),
    ],
)
async def test_class_characteristics(class_name, user_prompt, expected_stats):
    npc = await main(user_prompt)

    assert npc is not None
    assert isinstance(npc, NPC)
    assert npc.npc_class == class_name

    min_strength, max_strength = expected_stats["strength"]
    min_charisma, max_charisma = expected_stats["charisma"]
    min_intelligence, max_intelligence = expected_stats["intelligence"]

    assert min_strength <= npc.stats.strength <= max_strength, (
        f"{class_name.value} should have strength between {min_strength}-{max_strength}, "
        f"got {npc.stats.strength}"
    )
    assert min_charisma <= npc.stats.charisma <= max_charisma, (
        f"{class_name.value} should have charisma between {min_charisma}-{max_charisma}, "
        f"got {npc.stats.charisma}"
    )
    assert min_intelligence <= npc.stats.intelligence <= max_intelligence, (
        f"{class_name.value} should have intelligence between {min_intelligence}-{max_intelligence}, "
        f"got {npc.stats.intelligence}"
    )