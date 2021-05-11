#!/usr/bin/env python2
import sys
import os
import string
import random

DEBUG = 1

def whos_inside(in_house):
    if len(in_house) == 0:
        print("NOBODY HOME")
    else:
        to_return = ""
        for u in in_house:
            to_return +=  "%s, " % (u,)
        to_return = to_return[:-2]
        print(to_return)

def main(owner_name, keys):
    keys = set(keys)
    in_house = []
    inserted_key = None
    inserted_username = None

    if DEBUG:
        print("DEBUG:", "owner name", owner_name) #, "keys", keys

    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if line == "WHO'S INSIDE?":
            whos_inside(in_house)
        else:
            parsed = line.split(' ')
            if len(parsed) < 2:
                print("ERROR 1")
                continue
            if parsed[0] == "INSERT" and parsed[1] == "KEY":
                if len(parsed) != 4:
                    print("ERROR 2")
                    continue
                inserted_key = parsed[3]
                inserted_username = parsed[2]
                print("KEY", inserted_key, "INSERTED BY",  inserted_username)
            elif parsed[0] == "ENTER" and parsed[1] == "HOUSE":
                if len(parsed) != 3:
                    print("ERROR 3")
                    continue
                cur_user = parsed[2]

                if inserted_username != cur_user:
                    print("ACCESS DENIED 1")
                    continue

                if inserted_key == "FIREFIGHTER_SECRET_KEY":
                    print("ACCESS ALLOWED 1")
                elif cur_user.startswith("officer_with_warrant") and inserted_key == "POLICE_SECRET_KEY":
                    print("ACCESS ALLOWED 2")
                elif inserted_key in keys:
                    print("ACCESS ALLOWED 3")
                    if inserted_username == "attacker":
                        success()
                else:
                    print("ACCESS DENIED")
                    continue

                in_house.append(inserted_username)
                inserted_key = None
                inserted_username = None

            elif parsed[0] == "CHANGE" and parsed[1] == "LOCKS":
                if len(parsed) < 3:
                    print("ERROR")
                    continue
                change_locks_name = parsed[2]
                #print change_locks_name, owner_name, in_house
                if change_locks_name == owner_name:
                    keys = parsed[3:]
                    print("OK")
                else:
                    print("ACCESS DENIED")

            elif parsed[0] == "LEAVE" and parsed[1] == "HOUSE":
                if len(parsed) != 3:
                    print("ERROR")
                    continue
                user_to_leave = parsed[2]
                if not user_to_leave in in_house:
                    print(user_to_leave, "NOT HERE")
                else:
                    in_house.remove(user_to_leave)
                    print("OK")


def success():
    print("Congratulations, you successfully broke this level!")
    print ("Executing /usr/local/bin/l33t")
    print ("")
    os.system("/usr/local/bin/l33t")
    sys.exit(0)


if __name__ == '__main__':
    print("Your goal is to enter the house using the name \"attacker\" without using the firefighter key.")
    print("When you do, the `success` funciton will be called and you'll successfull break this level.")
    print("Good luck!")
    print("")

    # Generate a random owner name
    owner_name = "".join([random.choice(string.ascii_letters) for i in range(10)])

    # Generate a random key
    keys = [ "".join([random.choice(string.printable) for i in range(20)]) ]
    
    print(keys)
    
    main(owner_name, keys)
