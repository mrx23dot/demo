# pip install Pillow

from PIL import Image
import random

img = Image.new( 'RGB', (255,255), "black") # create a new black image
pixels = img.load() # create the pixel map
# operatorsa http://pillow.readthedocs.io/en/3.4.x/reference/Image.html?highlight=image%20access

cntX = 0
cntY = 0
for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
#        pixels.putpixel((i,j), 1)
        # http://pillow.readthedocs.io/en/3.4.x/reference/PixelAccess.html?highlight=PixelAccess
#        pixels[i,j] = (255,255,255) # set the colour accordingly
        pixels[i,j] = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)) # set the colour accordingly
        # pixels[x,y] = (R0-255,G0-255,B0-255)
        cntX = (cntX+1)%2
        cntY = (cntY+1)%2

img.save("out.jpg")
img.show()
