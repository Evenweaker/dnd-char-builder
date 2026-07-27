"""Application paths — works from source and from a frozen executable."""

from __future__ import annotations

import sys
from pathlib import Path


APP_NAME = "dnd-char-builder"
VERSION = "1.0.0"


def app_root() -> Path:
    """Directory that contains the app (or the executable)."""
    if getattr(sys, "frozen", False):
        # PyInstaller one-file / one-dir
        return Path(sys.executable).resolve().parent
    # Running from source: project root (parent of core/)
    return Path(__file__).resolve().parent.parent


def resource_root() -> Path:
    """Where bundled read-only resources live (data modules are imported, not files)."""
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return app_root()


def user_data_dir() -> Path:
    """
    Writable data (characters, drafts, exports).
    Next to the executable when frozen (portable),
    or under the project folder when running from source.
    """
    base = app_root()
    return base


def characters_dir() -> Path:
    d = user_data_dir() / "characters"
    d.mkdir(parents=True, exist_ok=True)
    return d


def drafts_dir() -> Path:
    d = user_data_dir() / "drafts"
    d.mkdir(parents=True, exist_ok=True)
    return d


def exports_dir() -> Path:
    d = user_data_dir() / "exports"
    d.mkdir(parents=True, exist_ok=True)
    return d
