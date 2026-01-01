from .file_mainbody import CharMainBody, load as mainbody_load

from .file_subclasses import Villager, Melee, Magic, Agile, load as subclass_Load

from .file_tiers import gen_tier, load as tiers_load

SUBCLASSES = (Villager, Melee, Magic, Agile)
LOADER = [mainbody_load,subclass_Load,tiers_load]

__all__ = [SUBCLASSES, LOADER]
