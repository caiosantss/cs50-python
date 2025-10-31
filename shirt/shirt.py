from PIL import Image

with Image.open("before1.jpg") as image:
    print(image.format, image.size, image.mode)
    #Crop porporcional - com save na propria imagem usando nome diferente
    # image.thumbnail((600, 600))
    # image.save("thumbnail before1 600.jpg")
