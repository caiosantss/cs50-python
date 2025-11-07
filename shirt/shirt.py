from PIL import Image
from PIL import ImageOps
import sys


"""
1- Expect exactly 2 command-line arguments
2 - file do not end in[.jpg, .jpeg, .png] - case-insensitively
3- both command-line does not have the same file extension
4- if the specified input does not exist: try / except at with
"""


def main():

    is_argv_valid()
    #SHIRT
    try:
        with Image.open(str(sys.argv[1])) as ImgBefore, Image.open(
            "shirt.png"
        ) as shirtImg:
            # print(shirtImg.size)
            shirtSize = shirtImg.size
            fitted = ImageOps.fit(ImgBefore, shirtSize)
            fitted.paste(shirtImg, mask=shirtImg)
            fitted.save(str(sys.argv[2]))
    except FileNotFoundError:
        sys.exit("Input does not exist")


def is_argv_valid():
    extension = (".png", ".jpg", ".jpeg")

    if len(sys.argv) != 3:
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        else:
            sys.exit("Too few command-line arguments")
    else:
        if not (sys.argv[2].lower().endswith(extension)):
            sys.exit(f"Invalid output")
        else:
            """
            rsplit(".",1)[-1] : da direita para esquerda, separa no primeiro ponto, somente uma vez e aloca na variavel o ultimo argumento da lista. ex: "("File.de.parana","png)
            """
            extensao1 = sys.argv[1].rsplit(".", 1)[-1]
            extensao2 = sys.argv[2].rsplit(".", 1)[-1]
            if not (extensao1.lower() == extensao2.lower()):
                sys.exit("Input and output have different extensions")


main()
