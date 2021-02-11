alphaList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]

def takeInput():
    user_input = input("Enter something to encrypt or decrypt: ")
    return user_input

def printMenu(): pass

def encrypt(userInput, key):
    cipher = ""
    for i in range(userInput):
        result = userInput[i].isalpha()
        if result:
            indexPos = alphaList.index(userInput[i])
            enIndex  = (indexPos + key) % 26
            cipher = cipher + alphaList[enIndex]
        else:
            cipher = userInput[i]

    return cipher



def main():
    user_input = takeInput()
    print("Size of user string: " + str(len(user_input)))
    print("Check for letters: " + str(user_input.isalpha()))
    print("End of program")

main()
