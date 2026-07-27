#!/usr/bin/env bash
# Build a standalone executable with PyInstaller
# Usage: ./build.sh
set -e
cd "$(dirname "$0")"

echo "==> Checking dependencies..."
python3 -c "import reportlab" 2>/dev/null || {
  echo "Installing reportlab..."
  pip3 install --user reportlab
}
python3 -c "import PyInstaller" 2>/dev/null || {
  echo "Installing PyInstaller..."
  pip3 install --user pyinstaller
}

echo "==> Building standalone binary..."
rm -rf build dist *.spec

python3 -m PyInstaller \
  --onefile \
  --name dnd-char-builder \
  --console \
  --clean \
  --noconfirm \
  --hidden-import=reportlab \
  --hidden-import=reportlab.pdfgen \
  --hidden-import=reportlab.lib \
  --hidden-import=core.character \
  --hidden-import=core.paths \
  --hidden-import=data.races \
  --hidden-import=data.classes \
  --hidden-import=data.backgrounds \
  --hidden-import=ui.terminal \
  main.py

echo ""
echo "==> Done!"
echo "Binary:  $(pwd)/dist/dnd-char-builder"
echo ""
echo "You can copy dist/dnd-char-builder anywhere and run it."
echo "Characters, drafts and exports are saved next to the binary."
