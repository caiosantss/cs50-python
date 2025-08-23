def main():
    question = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

    if questionOfLife(question):
        print("Yes")
    else:
        print("No")



def questionOfLife(txt):
    ##Tratamento da string strip - espaço em branco, lower - mionusculo - replace substitui
    normalized = txt.strip().lower().replace("-", " ")

    return normalized in ["42", "forty-two", "forty two"]

main()
