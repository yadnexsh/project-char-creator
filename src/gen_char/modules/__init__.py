from .rarity.rarity_tiers import Legendry, Epic, Rare, Common
from .character.char_type import Villager, Melee, Magic, Agile

ALL_CHARACTERS = [ Villager, Melee, Magic, Agile ]
ALL_RARITIES = [ Legendry, Epic, Rare, Common ]

NEUTRALS = [ Rare, Common]


__all__ = [ ALL_CHARACTERS, Legendry, Epic, Rare, Common ]