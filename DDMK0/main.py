from func import *
from func import observe
from users import *

# load in data:

while True:
    userInput = input("Input function: ")

    if userInput == "create": # creates a user
        userName = input("Input username: ") # eventually automatically makes a profile
        create(userName)

    elif userInput == "check":
     # choose which user to check
        checkUser(input("Which user?: "))

    elif userInput == "add":
        addTimeOnline(input("Which user?: "), input("How much time?: "))

    elif userInput == "data": # returns data structure
        print(users)

    elif userInput == "exit":
        saveData()
        quit()

    elif userInput == "delete":
        delete(input("Input user to delete: "))

    elif userInput == "reset":
        resetUsers()

    elif userInput == "observe":
        observe(input("Username: "))

    elif userInput == "stopObserve":
        stopObserve(input("Username: "))

    else:
        print("Invalid input, try again")



    #debug

        