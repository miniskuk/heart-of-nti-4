"""Ger ALLA Argentinas karaktärer (ledare, generaler, amiraler, rådgivare, forskare) katt-/hundbilder.

Skriver i OUT (modmapp):
  common/characters/ARG.txt        kopia av spelets fil där varje porträtt pekar på en egen sprite
  interface/nti4_argentina.gfx     sprite-definitioner
  och listar texturer att skapa i OUT/../arg_textures.txt (sökväg, bild-id, storlek)
"""
import re, sys, os
GAME, OUT, LIST = sys.argv[1], sys.argv[2], sys.argv[3]
IMGS = [i for i in sys.argv[4].split(',')]
src = open(os.path.join(GAME, 'common/characters/ARG.txt'), encoding='utf-8-sig').read()

out = []; pos = 0; depth = 0; char = None; ci = -1; sprites = []; tex = []
for m in re.finditer(r'([A-Za-z0-9_]+)\s*=\s*\{|\{|\}|\b(large|small)(\s*=\s*)("?)([^\s"}]+)("?)', src):
    if m.group(2):
        if depth >= 3 and char:
            kind = m.group(2); img = IMGS[ci % len(IMGS)]
            name = f'GFX_nti4_{char}_{kind}'
            path = f'gfx/leaders/NTI4ARG/{char}_{kind}.dds'
            if name not in sprites:
                sprites.append(name); tex.append((path, img, '156x210' if kind == 'large' else '65x67'))
            out.append(src[pos:m.start()] + f'{kind} = {name}'); pos = m.end()
        continue
    s = m.group(0)
    if s.endswith('{'):
        depth += 1
        if depth == 2: char = m.group(1); ci += 1
    else:
        depth -= 1
        if depth == 1: char = None
out.append(src[pos:])
os.makedirs(os.path.join(OUT, 'common/characters'), exist_ok=True)
open(os.path.join(OUT, 'common/characters/ARG.txt'), 'w', encoding='utf-8').write(''.join(out))
os.makedirs(os.path.join(OUT, 'interface'), exist_ok=True)
with open(os.path.join(OUT, 'interface/nti4_argentina.gfx'), 'w') as g:
    g.write('spriteTypes = {\n')
    for n, (p, _, _) in zip(sprites, tex):
        g.write(f'\tspriteType = {{\n\t\tname = "{n}"\n\t\ttexturefile = "{p}"\n\t}}\n')
    g.write('}\n')
with open(LIST, 'w') as f:
    for p, i, sz in tex: f.write(f'{p} {i} {sz}\n')
print('karaktärer:', ci + 1, 'sprites:', len(sprites))
