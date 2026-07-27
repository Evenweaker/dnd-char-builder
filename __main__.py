"""Allow: python3 -m dnd_char_builder  (when parent is on PYTHONPATH)
or from inside this folder: python3 -m main is not ideal; use run.sh.
"""
from main import main_menu

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        from ui.terminal import clear
        clear()
        print("\nInterrupted. Farewell.\n")
