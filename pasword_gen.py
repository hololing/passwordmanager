#Password generator
#Made by Emil Sležis


# module imports

import string
import random

#Lists with symbols

letters = list(string.ascii_letters)
digits = list(string.digits)
symbols = list(string.punctuation)

Characters = (letters, digits, symbols) 

# Generate password


def main():

    action = input("Enter your action (s - see, c - create new - m - modify)")

    if action == "s":

        readPassword()

        continueProg()
        
    elif action == "c":       

        generatePassword()

        continueProg()
  
    elif action == "m":

        modify = (input("Enter in which way you want to modify(c - change data d - delete data profile)"))

        if modify == "d":

            deleteProfile()

        elif modify == "c":

            print("Sorry this feature is not available at the moment.")

        else:

            invalidCharacter()

        continueProg()

    else:

        invalidCharacter()
        
    
def generatePassword():

    #Get data

    key = (input("Enter key of your password: "))
    email = (input("Enter your email: "))
    nick = (input("Enter your nickname: "))
    
    #Generate password
    
    passwordList = []

    for i in range(20):

        charType = random.choice(Characters)
        newChar = random.choice(charType)
        passwordList.append(newChar)
        

    password = ''.join([str(elem) for elem in passwordList])
    print(password)

    #Write data

    text_file = open("passwords.txt", "a") 

    text_file.write(key)
    text_file.write(" ")
    text_file.write(email)
    text_file.write(" ")
    text_file.write(nick)
    text_file.write(" ")
    text_file.write(password)
    text_file.write("\n")

    text_file.close()


def readPassword():

    needed = str(input("Enter what you want: "))
    
    with open('passwords.txt', 'r') as document:
        answer = {}
        for line in document:
            line = line.split()
            if not line:  # empty line?
                continue
            answer[line[0]] = line[1:]

    allData = (answer[needed])

    print("Email: " + allData[0])
    print("Nickname: " + allData[1])
    print("Password: " + allData[2])

def deleteProfile():

    nProfile = (input("Enter profile you want to delete"))
    
    
    
    with open("passwords.txt", "r") as f: 
        
        #Make profile

        answer = {}
        for line in f:
            line = line.split()
            if not line:  # empty line?
                continue
            answer[line[0]] = line[1:]

        allData = (answer[nProfile])

        cprofile = (nProfile, " ", allData[0], " ", allData[1], " ", allData[2])

        # read data line by line  
        data = f.readlines() 
      
    # open file in write mode 
    with open("passwords.txt", "w") as f: 
      
        for line in data : 
          
            # condition for data to be deleted 
            if line.strip("\n") != cprofile :  
                f.write(line) 

def invalidCharacter():

    print("wrong character")
        
    tryAgain = input("Do you want to try again?(y - yes, n - no)")

    if tryAgain == "y":
        main()

def continueProg():

    answer = (input("Do you want to do something else?(y - yes, n - no)"))

    if answer == "y" or answer == "yes":

        main()
    
main()