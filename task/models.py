from enum import Enum
from pydantic import BaseModel, Field


class Class(str, Enum):
    WARRIOR = "Warrior"
    MAGE = "Mage"
    ROGUE = "Rogue"
    MERCHANT = "Merchant"
    CLERIC = "Cleric"
    BARD = "Bard"
    COMMONER = "Commoner"
    MONSTER = "Monster"


class Stats(BaseModel):
    strength: int = Field(ge=1, le=20, description="Physical power (1-20)")
    charisma: int = Field(ge=1, le=20, description="Social influence (1-20)")
    intelligence: int = Field(ge=1, le=20, description="Mental acuity (1-20)")


class NPC(BaseModel):
    """
    Represents a NPC in a fantasy RPG.

    Example:
        {
            "name": "Eldrin the Wise",
            "npc_class": "Mage",
            "is_hostile": false
            "catchphrase": "Knowledge is the greatest power of all!",
            "stats": {
                "strength": 8,
                "charisma": 14,
                "intelligence": 18
            },
        }
    """

    name: str = Field(description="The full name of the character")
    npc_class: Class = Field(description="The character's profession or role")
    is_hostile: bool = Field(description="Whether the character is aggressive towards players")
    catchphrase: str = Field(description="A short, memorable quote typical of this character")
    stats: Stats = Field(description="Character attributes")
