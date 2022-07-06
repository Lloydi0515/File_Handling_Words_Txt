def JTOI():
    file = open("words.txt")
    data = file.read()
    for letter in data:
        if letter == 'J':
            print("I",end="")
        else:
            print(letter,end="")

    

JTOI()