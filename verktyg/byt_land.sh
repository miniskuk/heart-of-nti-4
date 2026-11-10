#!/usr/bin/env bash
# Byter alla ledarporträtt för ett land i HoI4 till en bild.
#
# Användning:
#   ./verktyg/byt_land.sh TAG bild.png STOR_CROP LITEN_CROP [sökord ...]
#
# Exempel (Schweiz):
#   ./verktyg/byt_land.sh SWI bilder/schweiz.png 760x1023+230+30 440x453+400+110 switzerland swiss
#
# STOR_CROP  = utsnitt för stora porträtt (ansikte + bröst), förhållande ca 156:210
# LITEN_CROP = utsnitt för små ikoner (bara ansiktet), ungefär kvadratiskt
# Format: BREDDxHÖJD+X+Y i pixlar från övre vänstra hörnet.
#
# Kräver: python3, ImageMagick 7 (magick).
# Miljövariabler:
#   HOI4_GAME = mappen där spelet ligger (har common/, gfx/, interface/)
#   MOD_DIR   = mappen med modden (standard: mods/miku_japan i detta repo)
set -euo pipefail

TAG=$1; IMG=$2; BIG=$3; SMALL=$4; shift 4
HERE=$(cd "$(dirname "$0")/.." && pwd)
GAME=${HOI4_GAME:-$HOME/.local/share/Steam/steamapps/common/Hearts of Iron IV}
MOD=${MOD_DIR:-$HERE/mods/miku_japan}
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

magick "$IMG" -crop "$BIG" +repage "$TMP/big.png"
magick "$IMG" -crop "$SMALL" +repage "$TMP/small.png"

# Hitta ledarnas bildfiler (alla versioner, även DLC). Delade standardbilder ersätts inte; ledaren får istället en egen bild via interface/nti4_ledare.gfx.
(cd "$GAME" && python3 -I "$HERE/verktyg/leaders.py" "$TAG" "$@") \
  > "$TMP/files.txt"

echo "Filer som byts:"; cat "$TMP/files.txt"

GFXFILE=$MOD/interface/nti4_ledare.gfx
while read -r f sz extra; do
  if [ "$f" = SPRITE ]; then
    # Ledaren använder en delad standardbild: ge spriten en egen textur i modden
    sprite=$sz; sz=$extra; f=gfx/leaders/NTI4/$sprite.dds
    mkdir -p "$MOD/interface"
    [ -s "$GFXFILE" ] || echo "spriteTypes = {" > "$GFXFILE"
    if ! grep -q "\"$sprite\"" "$GFXFILE"; then
      sed -i '$ d' "$GFXFILE" 2>/dev/null; grep -q '^spriteTypes' "$GFXFILE" || echo "spriteTypes = {" > "$GFXFILE"
      printf '\tspriteType = {\n\t\tname = "%s"\n\t\ttexturefile = "%s"\n\t}\n}\n' "$sprite" "$f" >> "$GFXFILE"
    fi
  fi
  h=${sz#*x}
  if [ "$h" -gt 150 ]; then src=$TMP/big.png; else src=$TMP/small.png; fi
  mkdir -p "$MOD/$(dirname "$f")"
  magick "$src" -alpha off -resize "${sz}^" -gravity center -extent "$sz" -alpha on \
    -define dds:compression=dxt5 -define dds:mipmaps=0 "DDS:$MOD/$f"
done < "$TMP/files.txt"

echo "Klart: $(wc -l < "$TMP/files.txt") bilder skrivna till $MOD"
