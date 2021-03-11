# REMEMBER: `distutils.version.*Version` types can be used to compare versions
# from strings like this.
# SMQTK prefers to use the strict numbering standard when possible.
__version__ = "0.16.0"

import abc
from .configuration import Configurable  # noqa: F401
from .plugin import Pluggable  # noqa: F401


class Plugfigurable (Pluggable, Configurable, metaclass=abc.ABCMeta):
    """
    When you don't want to have to constantly inherit from two mixin classes
    all the time, we provide this as a convenience that descends from both
    mixin classes: Pluggable and Configurable.
    """
