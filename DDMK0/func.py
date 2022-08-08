from operator import truediv
from users import *
from pickle import *
from time import monotonic
from datetime import datetime

"""
Ping losers lmao - Xingyu
"""

" CREATION FUNCTIONS: "

# VARIABLES

userNum = 0
runTime = 0

def create(name): # creates user and adds to hashmap
    currentUser = user(name)
    users[name] = currentUser

    # DATA TXT FILE EDITOR

" ACCESSING FUNCTIONS: "

def checkUser(tempUser): # outputs user stats

    seconds = str(tempUser.time_online)
    hours = str(int(tempUser.time_online / 3600))
    minutes = str(int((tempUser.time_online % 3600) / 60))
    userName = tempUser.name

    finalString = "Username is " + userName + "\n" + "They spent " + seconds + " seconds online" + "\n" + "or " + hours + " hours and " + minutes + " minutes" + "\n"

    return finalString

def checkUsers(user): # checks users dict for specific user. Returns true or false
    for key in users:
        if (user == key):
            return True
            
    return False




" EDITOR FUNCTIONS: "

def addTimeOnline(user, time):

    tempUser = users[user]

    tempUser.time_online += int(time)

" MEMORY ACCESSORS: "

pickle_in = open("data.pickle", "rb") #doesn't work without this
users = load(pickle_in)
pickle_in.close()

def saveData(): 
    global users
    pickle_out = open("data.pickle", "wb")
    dump(users, pickle_out)
    pickle_out.close()

def loadIn(): # FIXME
    pickle_in = open("data.pickle", "rb")
    global users 
    users = load(pickle_in)
    pickle_in.close()

def delete(user):
    del users[user]

def resetUsers():
    global users
    users = {}
    saveData()
    
"""
MAIN FUNCTIONS:
"""

def observe(user):

    print("hi")

    if (not(checkUsers(user))):
        create(user)

    if (users[user].loaded == True):
        print("User already being observed")

    else:

        currentUser = users[user]

        # User currently being observed
        currentUser.initTime = monotonic()
        increase()

def increase():
    global userNum
    userNum = userNum + 1
    print(f"User num is {userNum}")

def NUM():
    return userNum


def stopObserve(user):

    currentUser = users[user]

    finalTime = monotonic()
    tempTime = finalTime - currentUser.initTime
    sessionTime = int(tempTime)

    currentUser.time_online += sessionTime

    currentUser.loaded = False # User no longer being observed
    global userNum
    userNum = userNum - 1

" Exit function: "

def done():
    print("uwu")
    f = open('readme', 'w')
    global users
    for i in users:
        user = users[i]
        if (user.loaded):
            stopObserve(i)
            print(i)

    for i in users:
        user = users[i]
        print(user.loaded)
