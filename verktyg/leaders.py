"""Hittar ledarporträtt för ett land i HoI4.

Körs från spelmappen:  python3 -I leaders.py TAG [sökord ...]

Skriver ut rader:
  gfx/.../fil.dds WxH         -> textur som ska ersättas (alla definitioner, även DLC)
  SPRITE GFX_namn WxH          -> ledaren använder en delad standardbild; ge spriten en egen textur
"""
import re, glob, os, struct, sys

TAG = sys.argv[1]; KW = sys.argv[2:]
roots = ['.'] + sorted(glob.glob('dlc/*')) + sorted(glob.glob('integrated_dlc/*'))

gfx = {}  # sprite -> alla texturer den definieras med (bas + DLC)
for r in roots:
    for f in glob.glob(r + '/interface/*.gfx'):
        g = open(f, encoding='utf-8-sig', errors='ignore').read()
        for nm, tf in re.findall(r'name\s*=\s*"?([A-Za-z0-9_]+)"?\s*texturefile\s*=\s*"?([^"\s]+)"?', g):
            gfx.setdefault(nm, [])
            if tf not in gfx[nm]: gfx[nm].append(tf)

t = ''.join(open(f, encoding='utf-8-sig').read() for f in glob.glob(f'common/characters/{TAG}*.txt'))
chars = []; depth = 0
for m in re.finditer(r'([A-Za-z0-9_]+)\s*=\s*\{|\{|\}', t):
    s = m.group(0)
    if s.endswith('{'):
        depth += 1
        if depth == 2: start = m.start(); name = m.group(1)
    else:
        if depth == 2: chars.append((name, t[start:m.end()]))
        depth -= 1

src = ''.join(open(f, encoding='utf-8-sig', errors='ignore').read()
              for f in glob.glob('events/*.txt') + glob.glob('common/**/*.txt', recursive=True) if 'characters' not in f)
used = set(re.findall(r'(?:add_country_leader_role|promote_character)[^}]{0,150}?(\b' + TAG + r'_[a-z_]+)', src))

sprites = {}
for n, b in chars:
    if 'country_leader' in b or n in used:
        print('#', n, file=sys.stderr)
        for s in re.findall(r'(?:large|small)\s*=\s*"?([^\s"}]+)', b): sprites[s] = n
for f in glob.glob('events/*.txt') + glob.glob('common/scripted_effects/*.txt') + glob.glob('common/national_focus/*.txt') + glob.glob('common/decisions/*.txt'):
    base = os.path.basename(f).lower()
    if not (re.search(r'(^|_)' + TAG.lower() + r'[_.]', base) or any(k in base for k in KW)): continue
    tt = open(f, encoding='utf-8-sig', errors='ignore').read()
    for m in re.finditer(r'create_country_leader\s*=\s*\{', tt):
        p = re.search(r'picture\s*=\s*"?([^\s"}]+)', tt[m.end():m.end() + 800])
        if p: sprites[p.group(1)] = 'event'; print('# event', os.path.basename(f), p.group(1), file=sys.stderr)

SHARED = re.compile(r'generic|placeholder|leaders/(europe|asia|arabia|africa|southamerica|south_america|latin)', re.I)

def size(tf):
    sf = next((r + '/' + tf for r in roots if os.path.exists(r + '/' + tf)), None)
    if not sf or not sf.lower().endswith('.dds'): return None
    h, w = struct.unpack('<II', open(sf, 'rb').read(20)[12:20])
    return f'{w}x{h}'

out = set()
for s in sprites:
    tfs = gfx.get(s, [s])
    if not any(tf.lower().endswith(('.dds', '.tga', '.png')) for tf in tfs):
        print('OLÖST', s, file=sys.stderr); continue
    own = [tf for tf in tfs if not SHARED.search(tf)]
    for tf in own:
        sz = size(tf)
        if sz: out.add((tf, sz))
        else: print('SAKNAS', tf, file=sys.stderr)
    if not own and not SHARED.search(s):
        # spriten pekar bara på en delad bild: ge den en egen textur via modden
        sz = next((size(tf) for tf in tfs if size(tf)), None)
        if sz: out.add(('SPRITE ' + s, sz))
for tf, sz in sorted(out): print(tf, sz)
