"""Animated menu loop."""

import os
import sys
import time
import select
import termios
import tty
from typing import Optional, Tuple, List
from ui.dragons import DRAGON_FRAMES
from ui.input_helpers import parse_special, clear, HELP_TEXT

def flush_input():
    """Discard any pending keystrokes (e.g. leftover Enter after single-key input)."""
    fd = sys.stdin.fileno()
    try:
        import fcntl
        flags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)
        try:
            while True:
                if not sys.stdin.read(1):
                    break
        except (BlockingIOError, OSError):
            pass
        fcntl.fcntl(fd, fcntl.F_SETFL, flags)
    except Exception:
        while True:
            r, _, _ = select.select([sys.stdin], [], [], 0)
            if not r:
                break
            try:
                sys.stdin.read(1)
            except Exception:
                break


def getch(timeout: float = None) -> Optional[str]:
    """Read a single character without waiting for Enter."""
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setcbreak(fd)
        if timeout is None:
            ch = sys.stdin.read(1)
            return ch
        r, _, _ = select.select([sys.stdin], [], [], timeout)
        if r:
            return sys.stdin.read(1)
        return None
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def animated_menu_choice(title: str, options: List[str], delay: float = 0.14) -> Tuple[Optional[int], Optional[str]]:
    """Main-menu style loop: continuously animates the dragon while waiting for input."""
    frame_idx = 0
    n = len(DRAGON_FRAMES)
    max_opt = len(options)

    while True:
        clear()
        print(DRAGON_FRAMES[frame_idx])
        print("=" * 50)
        print(f"  {title}")
        print("=" * 50)
        print(HELP_TEXT)
        print()
        for i, opt in enumerate(options, 1):
            print(f"  {i}. {opt}")
        print()
        print("  Press a number (no Enter needed)")
        print("Select: ", end="", flush=True)

        frame_idx = (frame_idx + 1) % n

        ch = getch(timeout=delay)
        if ch is None:
            continue

        if ch == "\x03":
            raise KeyboardInterrupt
        if ch in ("\n", "\r", ""):
            flush_input()
            continue

        special = parse_special(ch)
        if special:
            flush_input()
            return None, special

        if ch.isdigit():
            val = int(ch)
            if 1 <= val <= max_opt:
                print(ch)
                time.sleep(0.08)
                flush_input()
                return val, None
