from pathlib import Path
from typing import Any


type Includes = dict[str, list[Path]]
type SectionOptions = str | list | tuple
type ConfigResponse = dict[str, Any] | list[dict[str, Any]]
type Nothing = None
