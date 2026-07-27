"""Terminal UI — re-exports for compatibility."""

from ui.dragons import DRAGON, DRAGON_SMALL, DRAGON_FRAMES
from ui.input_helpers import (
    CMD_BACK, CMD_RESET, CMD_QUIT, CMD_SAVE, HELP_TEXT,
    clear, banner, pause, parse_special, get_raw, get_int,
    choose_from_list, show_preview,
)
from ui.menu_anim import flush_input, getch, animated_menu_choice

__all__ = [
    "CMD_BACK", "CMD_RESET", "CMD_QUIT", "CMD_SAVE", "HELP_TEXT",
    "DRAGON", "DRAGON_SMALL", "DRAGON_FRAMES",
    "clear", "banner", "pause", "parse_special", "get_raw", "get_int",
    "choose_from_list", "show_preview",
    "flush_input", "getch", "animated_menu_choice",
]
