from PIL import Image

im = Image.open('37.jpg')
im.convert('RGB')

width = im.size[0]
height = im.size[1]

for x in range(width):
	for y in range(height):
		pixel = im.getpixel((x, y))
		ave = sum(pixel)/len(pixel)
		ave = int(ave)
		if (pixel[0]>100) and (pixel[1]<45) and (pixel[2]<45):
			im.putpixel((x, y), (pixel[0]+20,pixel[1]-50,pixel[2]-50))
		else:
			im.putpixel((x, y), (ave,ave,ave))
im.save('out3.jpg')
