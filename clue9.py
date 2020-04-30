import wave
from PIL import Image

wav = wave.open('untitled.wav')
width = 2000
height = 1000
img = Image.new('RGB', (width, height))

wav.setpos(2)
px = [0, 0, 0]
for i, frame in enumerate(wav.readframes(wav.getnframes())):
    px[i%3] = frame
    if i%3 == 2:
        img.putpixel((i//3%width, height - i//3//width - 1), tuple(px))
img.show()
