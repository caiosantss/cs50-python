from PIL import Image

with Image.open("shirt.png") as image:
    print(image.format, image.size, image.mode)
