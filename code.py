import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.GP18,10)

pixels.fill((255, 0, 0))


def delay(a):
    time.sleep(a)


def hex2rgb(color):
    hexx = color.lstrip("#")
    r = 0
    g = 0
    b = 0

    r = int(hexx[0:2], 16)
    g = int(hexx[2:4], 16)
    b = int(hexx[4:6], 16)

    rgb = (r,g,b)
    return rgb


def color(hexcol):
    pixels.brightness = 1
    pixels.fill(hex2rgb(hexcol))


color_file = open("rgb.cols")

while True:
    color_file.seek(0,0)
    for line in color_file.read().splitlines():
        command = line.split(" ")[0]
        if command == "c":
            color(line.split(" ")[1])
        elif command == "d":
            delay(float(int(line.split(" ")[1]))/1000)
