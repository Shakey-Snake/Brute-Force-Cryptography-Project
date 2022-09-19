import string

class Vigenere_Cypher():
   
    alphabet =  list(string.ascii_lowercase)

    def encrypt(key, message):

        lengthKey = len(key)
        lengthMessage = len(str(message))

        if lengthMessage < lengthKey:
            diff = lengthKey - lengthMessage
            key = key[diff:]
            print(key)

        elif lengthMessage > lengthKey:

            remainder = lengthMessage % lengthKey
            temp = key

            while lengthKey < lengthMessage:
                temp = temp + key
                lengthKey = len(temp)

            key = temp

            if lengthKey != lengthMessage:
                key = key[:lengthMessage]
                lengthKey = len(key)
        
        encryptedMessage = ""
        print(key)
        print(message)

        for idx, i in enumerate(message):
            messageLetterNum = ord(i) - 96
            keyLetterNum = ord(key[idx]) - 96
            
            encryptedLetter = ((messageLetterNum + keyLetterNum) % 26) + 96
            encryptedMessage = encryptedMessage + chr(encryptedLetter)
        
        return encryptedMessage

            
    if __name__ == "__main__":
        message = input("Enter message: ").lower()
        key = input("Enter key: ").lower()
        encryptedMessage = encrypt(key, message)
        print(encryptedMessage)