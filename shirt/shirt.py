from PIL import Image

with Image.open("before1.jpg") as image:
    print(image.format, image.size, image.mode)
    new_image_before1 = image.thumbnail((600, 600))
    new_image_before1.save("New_thumbnail_before1_resize.jpg")
