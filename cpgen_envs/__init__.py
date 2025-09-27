import sys
import cpgen_envs.environments.manipulation.single_arm_env as patched_module
sys.modules['robosuite.environments.manipulation.single_arm_env'] = patched_module


import cpgen_envs.environments.manipulation.nut_assembly
from cpgen_envs.environments.manipulation.hammer_cleanup import (
    HammerCleanup_D0 as HammerCleanup_D0,
)
from cpgen_envs.environments.manipulation.hammer_cleanup import (
    HammerCleanup_D1 as HammerCleanup_D1,
)
from cpgen_envs.environments.manipulation.mug_cleanup import (
    MugCleanup_D0 as MugCleanup_D0,
)
from cpgen_envs.environments.manipulation.mug_cleanup import (
    MugCleanup_D1 as MugCleanup_D1,
)
from cpgen_envs.environments.manipulation.nut_assembly import (
    NutAssembly_D0 as NutAssembly_D0,
)
from cpgen_envs.environments.manipulation.nut_assembly import (
    NutAssembly_D1 as NutAssembly_D1,
)
from cpgen_envs.environments.manipulation.nut_assembly import (
    Square_D0 as Square_D0,
    Square_D1 as Square_D1,
    # Square_D2 as Square_D2,
    SquareWide as SquareWide,
    # SquareReal as SquareReal
)
from cpgen_envs.environments.manipulation.three_piece_assembly import (
    ThreePieceAssembly as ThreePieceAssembly,
)
from cpgen_envs.environments.manipulation.coffee import (
    Coffee_D1 as Coffee_D1,
)
from cpgen_envs.environments.manipulation.coffee import (
    Coffee_D2 as Coffee_D2,
)
from cpgen_envs.environments.manipulation.threading import (
    Threading_D2 as Threading_D2,
)
from cpgen_envs.environments.manipulation.kitchen import (   
    Kitchen_D0 as Kitchen_D0,
)
from cpgen_envs.environments.manipulation.kitchen import (   
    Kitchen_D1 as Kitchen_D1,
)
from cpgen_envs.environments.manipulation.kitchen import (   
    KitchenWide as KitchenWide,
)
from cpgen_envs.environments.manipulation.stack import (   
    StackThreeWide as StackThreeWide,
)
from cpgen_envs.environments.manipulation.pouring import (   
    Pouring as Pouring,
)
from cpgen_envs.environments.manipulation.mug_hanging import (   
    MugHanging as MugHanging,
)
from cpgen_envs.environments.manipulation.wine_glass_hanging import (   
    WineGlassHanging as WineGlassHanging,
)
from mimicgen.envs.robosuite.pick_place import (
    PickPlace_D0 as PickPlace_D0,
)

# override robosuite files
from robosuite.models.objects.xml_objects import (
    CanObject as CanObject,
    CerealObject as CerealObject,
    MilkObject as MilkObject,
)

# register grippers
from cpgen_envs.models.grippers.panda_umi_gripper import PandaUmiGripper as PandaUmiGripper

from robosuite.models.objects.xml_objects import MujocoXMLObject
import pathlib

def can_obj_init(self, name):
    MujocoXMLObject.__init__(
        self,
        pathlib.Path(cpgen_envs.__file__).parent / "models" / "assets" / "objects" / "can.xml",
        name=name,
        joints=[dict(type="free", damping="0.0005")],
        obj_type="all",
        duplicate_collision_geoms=True,
    )

def cereal_obj_init(self, name):
    MujocoXMLObject.__init__(
        self,
        pathlib.Path(cpgen_envs.__file__).parent / "models" / "assets" / "objects" / "cereal.xml",
        name=name,
        joints=[dict(type="free", damping="0.0005")],
        obj_type="all",
        duplicate_collision_geoms=True,
    )

def milk_obj_init(self, name):
    MujocoXMLObject.__init__(
        self,
        pathlib.Path(cpgen_envs.__file__).parent / "models" / "assets" / "objects" / "milk.xml",
        name=name,
        joints=[dict(type="free", damping="0.0005")],
        obj_type="all",
        duplicate_collision_geoms=True,
    )

CanObject.__init__ = can_obj_init
CerealObject.__init__ = cereal_obj_init
MilkObject.__init__ = milk_obj_init

__version__ = "0.0.1"
