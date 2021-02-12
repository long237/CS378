alphaList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]

def takeInput():
    user_input = input("Enter something to encrypt or decrypt: ")
    return user_input

def getInt():
    user_input = input("Enter a key: ")
    while not user_input.isnumeric():
        user_input = input("Enter a key: ")
    return int(user_input)

def getOp():
    user_input = input("Enter an option: ")
    while (not user_input.isnumeric()) or (int(user_input) < 1) or (int(user_input) > 3):
        user_input = input("Enter an option: ")
    return user_input

def printMenu():
    print("1. Encrypt \n"
          "2. Decrypt \n"
          "3. Exit")

def convert(userInput, key, flag):
    reValue = ""

    if flag == 1:
        for i in range(len(userInput)):
            result = userInput[i].isalpha()

            #If it is a letter then shift the index therefore encrypt it
            if result:
                lowerBool = userInput[i].islower()
                userUpper = userInput[i].upper()
                indexPos = alphaList.index(userUpper)
                enIndex = (indexPos + key) % 26

                #if the letter was lower case, make it lower case again
                ciLetter = alphaList[enIndex]
                if lowerBool:
                    ciLetter = alphaList[enIndex].lower()
                reValue = reValue + ciLetter

            #not a letter just add to the cipher text
            else:
                reValue = reValue + userInput[i]


    #Decryption
    elif flag == 2:
        for i in range(len(userInput)):
            result = userInput[i].isalpha()

            # If it is a letter then shift the index therefore encrypt it
            if result:
                lowerBool = userInput[i].islower()
                userUpper = userInput[i].upper()
                indexPos = alphaList.index(userUpper)
                deIndex = (indexPos + (26 - key)) % 26

                ciLetter = alphaList[deIndex]
                if lowerBool:
                    ciLetter = alphaList[deIndex].lower()
                reValue = reValue + ciLetter

            # not a letter just add to the cipher text
            else:
                reValue = reValue + userInput[i]

    return reValue



def main():
    # user_input = takeInput()
    # userInt = getInt()
    # cipher = convert(user_input, 19, 1)
    # print("Size of user string: " + str(len(user_input)))
    # print("Cipher text:" + cipher)
    # print("End of program")

    user_op = -1
    while user_op != 3:
        printMenu()
        user_op = int(getOp())
        if user_op != 3:
            user_str = takeInput()
            user_key = getInt()
            out = convert(user_str, user_key, user_op)
            print("Output: " + out)
        else:
            print("Good bye")

main()
