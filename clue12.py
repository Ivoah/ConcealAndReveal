from PIL import Image
import functools
import re

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def msb(bytes):
    return functools.reduce(lambda a, b: (a << 8) | b, bytes)

def lsb(bytes):
    return msb(bytes[::-1])

with open('AragornHelmsDeepBattlePortrait.bmp', 'rb') as f:
    f.seek(0x12)
    width = lsb(f.read(4))
    height = lsb(f.read(4))
    f.seek(0x1c)
    bpp = lsb(f.read(2))
    # print((width, height))
    f.seek(0xA)
    offset = lsb(f.read(1))
    f.seek(offset)
    pixels = f.read()

extracted = ''.join(chr((b&0b11111) - 1 + ord('a')) for b in pixels)

with open('lotr.txt') as f:
    text = f.read().lower().replace('û', 'u').replace('ú', 'u')
    text = re.sub(r'[^a-z]', '', text)

open('a.txt', 'w').write(extracted)
open('b.txt', 'w').write(text)

for i, (e, t) in enumerate(zip(extracted, text)):
    if e != t:
        print(i)
        break
        print(e, end='')
