from PIL import Image

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

img = Image.open('TriangulumGalaxyFov.bmp')
start = (17, 499)
length = 69
start = img.width*start[1] + start[0]
message = ''.join(chr(c) for px in list(img.getdata())[start:start+length] for c in px)
for chunk in chunks(message, 4):
    chunk = list(chunk)
    chunk[0], chunk[2] = chunk[2], chunk[0]
    print(''.join(chunk), end='')
print()
