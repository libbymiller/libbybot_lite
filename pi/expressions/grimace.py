import time

from rgbmatrix5x5 import RGBMatrix5x5

rgbmatrix5x5 = RGBMatrix5x5()

rgbmatrix5x5.set_clear_on_exit()
rgbmatrix5x5.set_brightness(0.3)

colours = [
    (0xff, 0x00, 0x00),
    (0x00, 0xff, 0x00),
    (0x00, 0x00, 0xff),
    (0xff, 0xff, 0xff)
]


def grimace():
  r, g, b = colours[3]

  rgbmatrix5x5.set_pixel(2, 0, r, g, b)
  rgbmatrix5x5.set_pixel(2, 1, r, g, b)
  rgbmatrix5x5.set_pixel(2, 2, r, g, b)
  rgbmatrix5x5.set_pixel(2, 3, r, g, b)
  rgbmatrix5x5.set_pixel(2, 4, r, g, b)

  rgbmatrix5x5.set_pixel(3, 0, r, g, b)
  rgbmatrix5x5.set_pixel(3, 1, r, g, b)
  rgbmatrix5x5.set_pixel(3, 2, r, g, b)
  rgbmatrix5x5.set_pixel(3, 3, r, g, b)
  rgbmatrix5x5.set_pixel(3, 4, r, g, b)

  rgbmatrix5x5.set_pixel(4, 0, r, g, b)
  rgbmatrix5x5.set_pixel(4, 1, r, g, b)
  rgbmatrix5x5.set_pixel(4, 2, r, g, b)
  rgbmatrix5x5.set_pixel(4, 3, r, g, b)
  rgbmatrix5x5.set_pixel(4, 4, r, g, b)

  rgbmatrix5x5.show()

#grimace()
#time.sleep(2)
