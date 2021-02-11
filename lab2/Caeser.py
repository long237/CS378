alphaList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]

def takeInput():
    user_input = input("Enter something to encrypt or decrypt: ")
    return user_input

def getInt():
    user_input = input("Enter a key: ")
    while not user_input.isnumeric():
        user_input = input("Enter a key: ")
    return user_input

def printMenu(): pass

def convert(userInput, key, flag):
    reValue = ""

    if flag == 0:
        for i in range(len(userInput)):
            result = userInput[i].isalpha()

            #If it is a letter then shift the index therefore encrypt it
            if result:
                userUpper = userInput[i].upper()
                indexPos = alphaList.index(userUpper)
                enIndex = (indexPos + key) % 26
                reValue = reValue + alphaList[enIndex]

            #not a letter just add to the cipher text
            else:
                reValue = reValue + userInput[i]

    #Decryption
    elif flag == 1:
        for i in range(len(userInput)):
            result = userInput[i].isalpha()

            # If it is a letter then shift the index therefore encrypt it
            if result:
                userUpper = userInput[i].upper()
                indexPos = alphaList.index(userUpper)
                deIndex = (indexPos + (26 - key)) % 26
                reValue = reValue + alphaList[deIndex]

            # not a letter just add to the cipher text
            else:
                reValue = reValue + userInput[i]

    return reValue



def main():
    user_input = takeInput()
    userInt = getInt()
    cipher = convert(user_input, 2, 1)
    print("Size of user string: " + str(len(user_input)))
    print("Cipher text:" + cipher)
    print("End of program")

main()
