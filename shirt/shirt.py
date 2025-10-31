from PIL import Image

opening = Image.open("shirt.png")
size = opening.format("shirt.png")
print(size)
