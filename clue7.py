from PIL import Image
import functools

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def msb(bytes):
    return functools.reduce(lambda a, b: (a << 8) | b, bytes)

def lsb(bytes):
    return msb(bytes[::-1])

with open('MassivelyScaleableDataCenterPic.bmp', 'rb') as f:
    f.seek(0x12)
    width = lsb(f.read(4))
    height = lsb(f.read(4))
    f.seek(0x1c)
    bpp = lsb(f.read(2))
    print((width, height))
    f.seek(0xA)
    offset = lsb(f.read(1))
    f.seek(offset)
    pixels = f.read()

img = Image.new('1', (width, height))
for i, byte in enumerate(pixels[::3]):
    if byte&1:
        img.putpixel((i%width, height - i//width), True)
img.show()
