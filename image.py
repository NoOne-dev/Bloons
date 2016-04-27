from PIL import Image
from PIL import ImageGrab
"""before = Image.open("before.png")
after = Image.open("after.png")
bpix = before.load()
apix = after.load()

for x in range(before.size[0]):
	for y in range(before.size[1]):
		if bpix[x,y]==apix[x,y]:
			apix[x,y] = (255,255,255,255)

after.save("lol.png")
lol = Image.open("lol.png").convert("LA")
lol = lol.resize((10,10), Image.ANTIALIAS)
lol.save("lolg.png")
"""

def compare(im1, im2):
	pix1 = im1.load()
	pix2 = im2.load()
	error = 0
	for x in range(im1.size[0]):
		for y in range(im1.size[1]):
			if not pix1[x,y]==pix2[x,y]:
				error += 1
	return error/float(im1.size[0]*im1.size[1])

