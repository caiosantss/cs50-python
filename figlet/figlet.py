from pyfiglet import Figlet
import sys
import random


# Usar argv para pegar fonte: pegar 2 argumentos [1]: -f ou --font, [2]: nome da fonte
# Caso tenh 0 argumentos : random(font)
# Caso tenha argumentos e nao seja aqueles: sys.exit()
# input: texto str para ser mudado
# output: print(figlet.renderText(texto))

figlet = Figlet()


if len(sys.argv) > 1:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (
        sys.argv[2] in figlet.getFonts()
    ):
        figlet.setFont(font=str(sys.argv[2]))
        texto = str(input("Input: "))
        print(f"Output: {figlet.renderText(texto)}")
    else:
        sys.exit("Invalid usage")
else:
    figlet.setFont(font=random.choice(figlet.getFonts()))
    texto = str(input("Input: "))
    print(f"Output: {figlet.renderText(texto)}")
