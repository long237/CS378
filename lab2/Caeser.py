alphaList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]

def takeInput():
    user_input = input("Enter something to encrypt or decrypt: ")
    return user_input

def printMenu(): pass

def encrypt(userInput, key):
    cipher = ""
    for i in range(len(userInput)):
        result = userInput[i].isalpha()

        #If it is a letter then shift the index therefore encrypt it
        if result:
            userUpper = userInput[i].upper()
            #indexPos = alphaList.index(userInput[i].upper())
            indexPos = alphaList.index(userUpper)
            enIndex = (indexPos + key) % 26
            cipher = cipher + alphaList[enIndex]

        #not a letter just add to the cipher text
        else:
            cipher = cipher + userInput[i]

    return cipher



def main():
    user_input = takeInput()
    cipher = encrypt(user_input, 2)
    print("Size of user string: " + str(len(user_input)))
    print("Check for letters: " + str(user_input.isalpha()))
    print("Cipher text:" + cipher)
    print("End of program")

main()
