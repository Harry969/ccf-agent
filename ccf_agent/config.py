from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class AgentConfig:
    """Thin wrapper around the project JSON config."""

    path: Path
    data: dict[str, Any]

    @property
    def base_dir(self) -> Path:
        return self.path.parent

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def resolve_path(self, value: str | None) -> Path | None:
        if not value:
            return None
        path = Path(value)
        if path.is_absolute():
            return path
        candidate = (self.base_dir / path).resolve()
        if candidate.exists():
            return candidate
        return (ROOT / path).resolve()

    def read_text(self, value: str | None) -> str:
        path = self.resolve_path(value)
        if not path:
            return ""
        return path.read_text(encoding="utf-8")


def load_config(path: str | Path) -> AgentConfig:
    config_path = Path(path).resolve()
    with config_path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    return AgentConfig(path=config_path, data=data)
