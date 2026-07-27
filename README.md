# D&D 5e Character Builder

**Version 1.0.0**

A terminal character creator for *Dungeons & Dragons 5th Edition*  
(Player's Handbook + Essentials Kit content).

## Features

- Full race / subrace / class / background selection
- Ability scores: Standard Array or 4d6-drop-lowest
- Skills & starting equipment packages
- Racial traits and level-1 class features on the sheet
- **Live character sheet** while you build
- Save / load characters and **resumable drafts**
- Export to **text** or **PDF**
- Continuous animated dragon on the main menu
- Single-key menu navigation (no Enter needed for numbers)
- Back / Reset / Quit / Save draft at almost every prompt

## Quick start (from source)

```bash
cd dnd_char_builder
./run.sh
# or:
python3 main.py
```

Requires **Python 3.10+**.  
PDF export needs `reportlab`:

```bash
pip3 install --user reportlab
# or: pip3 install -r requirements.txt
```

## Build a standalone executable

On Linux (tested mindset: Q4OS / Debian-based):

```bash
./build.sh
```

This installs PyInstaller if needed and produces:

```
dist/dnd-char-builder
```

Copy that single file anywhere and run it — no Python install required on the target machine.

Characters, drafts and exports are stored **next to the binary** (portable).

Manual PyInstaller command (if you prefer):

```bash
pip3 install --user pyinstaller reportlab
pyinstaller --onefile --name dnd-char-builder --console main.py
```

## Project layout

```
dnd_char_builder/
├── main.py           # entry point + creation flow
├── run.sh            # launch from source
├── build.sh          # build standalone binary
├── core/             # Character model, paths, version
├── ui/               # terminal UI, animation, input
├── data/             # races, classes, backgrounds
├── characters/       # saved characters (JSON)
├── drafts/           # mid-creation drafts
├── exports/          # .txt / .pdf sheets
├── requirements.txt
├── pyproject.toml
└── LICENSE
```

## Controls (reminder)

| Key | Action |
|-----|--------|
| `1`–`9` | Choose menu option (no Enter) |
| `b` | Back one step |
| `r` | Reset character |
| `s` | Save draft |
| `q` | Quit to main menu |
| `k` / `a` | Keep / again (when rolling stats) |

## License

MIT — see `LICENSE`.

Dungeons & Dragons is a trademark of Wizards of the Coast. This is an unofficial fan tool.

## Open source

This project is free and open source under the **MIT License** (see `LICENSE`).

You can:
- use it for any purpose
- modify it
- share it
- build on it

Attribution is appreciated but not required beyond what MIT already asks (keep the license notice).

### Disclaimer

*Dungeons & Dragons* and related marks are trademarks of Wizards of the Coast.  
This is an **unofficial fan-made tool** and is not affiliated with or endorsed by Wizards of the Coast.

### DMCA / copyright contact

If you believe this project infringes your copyright, please send a notice to:

**Email:** `gilera3@gmail.com`

Include:
- your contact information
- a description of the copyrighted work
- the material you believe is infringing (and where it appears in this repo)
- a statement that you have a good-faith belief the use is not authorized
- a statement that the information in the notice is accurate
- your signature (physical or electronic)

We will review valid notices promptly. See also `DMCA.md`.

### Contributing

Ideas and pull requests are welcome. Useful directions:
- Point Buy ability scores
- Level-up support
- More complete spell lists
- Better PDF layout
- Windows/macOS builds

1. Fork the repo
2. Create a branch
3. Make your change
4. Open a pull request

### Publishing a release (maintainers)

```bash
# Source archive
git tag v1.0.0
git push origin v1.0.0

# Linux binary
./build.sh
# Upload dist/dnd-char-builder on the GitHub Release page
```
