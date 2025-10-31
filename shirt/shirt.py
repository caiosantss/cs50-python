from PIL import Image

opening = Image.open("shirt.png")
size = opening.size("shirt.png")
print(size)
