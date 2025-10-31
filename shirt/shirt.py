from PIL import Image

with Image.open("before1.jpg") as image:
    image.rotate(90).show()
