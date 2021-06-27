from typing import Dict, Optional

VARIABLE_STORAGE: Dict[str, Dict[str, float]] = {}

_CURRENT_VERSION: Optional[str] = None

USE_LATEX = True

from .variable import *

__version__ = "0.1.0"
