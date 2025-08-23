def main():
    txt = input("Write any text: ")
    txtConverted = convert(txt)
    print(txtConverted)


def convert(to):
    '''
  Old solution: replace method doesnt change the origina string, strings are imutable. He give us back a new string, but I'm not putting this string in any variable.

    if ":)" in to and ":(" in to:
           to.replace(":)", "🙂")
           to.replace(":(", "🙁")
      elif ":)" in to:
          to.replace(":)", "🙂")
      elif ":(" in to:
          to.replace(":(", "🙁")
           return to '''

    to =  to.replace(":)", "🙂")
    to =  to.replace(":(", "🙁")

    return to


main()
