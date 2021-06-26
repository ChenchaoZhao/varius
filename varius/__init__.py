from typing import Dict, Optional

from .variable import *

VARIABLE_STORAGE: Dict[str, Dict[str, float]] = {}

_CURRENT_VERSION: Optional[str] = None

__version__ = "0.1.0"
