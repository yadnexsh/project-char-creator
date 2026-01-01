from .file_mainbody import CharMainBody, load as mainbody_load

from .file_subclasses import Villager, Melee, Magic, Agile, load as subclass_Load
SUBCLASSES = (Villager, Melee, Magic, Agile)

from .file_tiers import gen_tier, load as tiers_load

LOADER = [mainbody_load,subclass_Load,tiers_load]