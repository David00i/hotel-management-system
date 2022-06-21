#-------------------------------------------------------------------------------
# Name:        Programs breaks into module by classes
# Purpose:     for python project
#
# Author:      Group 6
#
# Title:       Hotel Management System
#-------------------------------------------------------------------------------

import datetime                                        # in global
import json                                            # module import

class room:                                            # Parent room class
    """
    @AC
    Read and update room status"""
    def __init__(self):
        roomfile = open("room_status.txt","r")         # read files
        self.roomlist = roomfile.read()
        roomfile.close()
        self.roomlist = json.loads(self.roomlist)      # turn string into dictionary

    def updates(self,room_name,func):                  # func 1 to occupied, 0 to empty
        self.roomlist[room_name] = func                # Occupied by guest
        roomWfile = open("room_status.txt","w")
        result = json.dumps(self.roomlist)
        roomWfile.write(result)                        # updated
        roomWfile.close()

class guest:                                           # guest class
    """
    @AC
    Read and update guest info"""
    def __init__(self):
        guestfile = open("guest_info.txt","r")
        self.guestlist = guestfile.readlines()
        guestfile.close()
        for i in range (len(self.guestlist)):          # change string into dictionary
            self.guestlist[i] = json.loads(self.guestlist[i])

    def updates(self, newInfo):
        guestAfile = open("guest_info.txt","a")        # write files (append)
        result = json.dumps(newInfo)
        guestAfile.write(result)                       # write a new dict into file
        guestAfile.write("\n")
        guestAfile.close()

class check (room):                                    # Child check class
    """
    @Han
    Inheritance from room parent class and check available info"""
    def __init__(self):
        room.__init__(self)                            # automatically print out
        print("Here are the room types avaliable : ")  # when available function is called

    def available(self):
        sumABC = [0,0,0]                               # list that store available room
        for room in self.roomlist:
            if not self.roomlist[room]:                # if '0' means empty room
                if room[0] == 'A':                     # calculating the available room
                    sumABC[0] +=1
                elif room[0] == 'B':
                    sumABC[1] +=1
                elif room[0] == 'C':
                    sumABC[2] +=1
        return sumABC