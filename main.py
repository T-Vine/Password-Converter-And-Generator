from numpy import random

def generate(pStrength="high"):
    letters_Lower = [chr(i) for i in range(97, 123)] #creating lower case alphabet with ASCII
    letters_Upper =list(map(toUpper, letters_Lower)) #converting to Upper
    symbols = ["@","#","*","%","!"]
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    password = ""
    #if strength input, convert to lowercase
    try:
        pStrength = pStrength.lower()
    except:
        pass

    #assigning from text input
        
    if (pStrength == "high"):
        length = 18
    elif (pStrength == "medium"):
        length = 12
    elif (pStrength == "low"):
        length = 8

    else:
        length = pStrength
    for index in range(length):
        no = random.randint(0,4)
            
        if (no == 0):
            password = password + letters_Lower[random.randint(0, len(letters_Lower))]
        elif (no == 1):
            password = password + letters_Upper[random.randint(0, len(letters_Upper))]
        elif (no == 2):
            password = password + numbers[random.randint(0, len(numbers))]
        else:
            password = password + symbols[random.randint(0, len(symbols))]

            
    return password
                
def toUpper(current):
    return current.upper()


def conversion(pOldPass):
    symbolArr = ["@","#","*","%","!"]
    numbersArr = ["1","2","3","4","5","6","7","8","9","0"]
    
    converDict = { "a":"@",
                   "e":"3",
                   "i":"1",
                   "l":"!",
                   "o":"0"}



        
    symbols = 0
    integers = 0
    password = pOldPass
    newPass = ""
    index = 1
    if (len(password) < 7):
        return "Your word should be at least 6 characters long."
    else:        
        for character in password:
            try:
                
                if (random.randint(1,3) == 1): #making random
                    char = converDict[character.lower()] #converting if possible
                    newPass = newPass + str(char)
                else:
                    raise NameError #raising error to invoke exception and make sure we get the first character upper case
                #else:
                #    char = character
                #    newPass = newPass + char
                
                
            except:
                char = character
                if (index == 1):
                    newPass = newPass + char.upper()
                else:
                    newPass = newPass + char
                index += 1
                
        for character in newPass:
            if (character.isdigit()):
                integers += 1
            elif (not character.isalnum()):
                symbols += 1
            
        
        #if (symbols < 2):
        #    symbols = 2-symbols
        #if (integers < 2):
        #    integers = 2-integers

        print(symbols, integers)
        
        while (symbols < 1):
            if (random.randint(0,2) == 1):
                newPass = newPass + symbolArr[random.randint(0, len(symbolArr))]
                
            else:
                newPass = symbolArr[random.randint(0, len(symbolArr))] + newPass
            symbols += 1
            
                
        while (integers < 5):
            if (random.randint(0,2) == 1):
                newPass = str(numbersArr[random.randint(0, len(numbersArr))]) + newPass
                
                    
            else:
                newPass = newPass + str(numbersArr[random.randint(0, len(numbersArr))]) 
            integers += 1

        
                    
        return newPass
    
            
    
if (__name__ == "__main__"):
    entry = input("Enter Q to Exit. Enter A for a random password or B to convert a word into a password. \n")
    while (entry != "Q"):
        if (entry == "A"):
            print(generate())
            #break
        elif (entry == "B"):
            convert = input("Enter a word that you want to be converted into a password. Do NOT include letters or numbers. These will be added. \n")
            print(conversion(convert))
            #break
        else:
            print("Incorrect input")
            #break
        entry = input("Enter Q to Exit. Enter A for a random password or B to convert a word into a password. \n")
    print("Goodbye.")
    

    

