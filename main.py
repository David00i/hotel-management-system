#-------------------------------------------------------------------------------
# Name:        Module of Hotel Management System
# Purpose:     for python project
#
# Author:      Group 6
#
# Title:       Hotel Management System
#-------------------------------------------------------------------------------

# INFORMATION OF FILEs
# guest_info.txt
# room_status.txt
# receipt.txt

import datetime                 # in global
import json                     # @module import
import database                 # @module import
import opening                  # @module import
import closing                  # @module import

opening.hi()                    # Startup Animation from opening module
def MENU():
    print("""
---WELCOME TO GSIX HOTEL---
|   1\t|\tCHECK IN \t|
|   2\t|\tRECORDING \t|
|   3\t|\tPRINTOUT \t|
|   4\t|\tCHECK OUT \t|
    """)
    func_select = int(input("Enter the function number (Exit = 0):"))
    if func_select == 1:
        CHECK_IN()              # go to checkin function
    elif func_select == 2:
        RECORDING()             # go to recording function
    elif func_select == 3:
        PRINT_OUT()             # go to printout function
    elif func_select == 4:
        CHECK_OUT()             # go to checkout function
    elif func_select == 0:
        print("GOOD BYE!")      # exit program
    else:
        print("Errors")         # invalid input

def CHECK_IN():
    """
    @AC
        -> Check the current status of room
        -> Enter the information and then pass to recording()
    """
    print("\nCHECK IN!")
    r = database.room()
    c = database.check()
    sumABC = c.available()
    print("Room Premium \t(A)(RM250 per day)  = \t",sumABC[0])
    print("Room Standard \t(B)(RM200 per day)  = \t",sumABC[1])
    print("Room Single \t(C)(RM100 per day)  = \t",sumABC[2])
    ans = input("If want to continue the check in, enter y/Y: ")
    if ans == "y" or ans == "Y":
        print("\nThanks for choosing GSIX Hotel!")
        ans_room = input("Please select the room type (A, B, C): ")
        if ans_room == "A":
            if sumABC[0]!=0:
                rooms, name, contact, date = CHECKin(ans_room)
                recording (rooms, name, contact, date)
                MENU()
            else:
                print("This type of room is full, please select another type.")
                CHECK_IN()
        elif ans_room == "B":
            if sumABC[1]!=0:
                rooms, name, contact, date = CHECKin(ans_room)
                recording (rooms, name, contact, date)
                MENU()
            else:
                print("This type of room is full, please select another type.")
                CHECK_IN()
        elif ans_room == "C":
            if sumABC[2]!=0:
                rooms, name, contact, date = CHECKin(ans_room)
                recording (rooms, name, contact, date)
                MENU()
            else:
                print("This type of room is full, please select another type.")
                CHECK_IN()
        else:
            print("Error!")


def CHECKin(room_type):
    """
    @AC
    -> to obtain guest information"""
    r = database.room()
    for Room in r.roomlist:
        if Room[0] == room_type and r.roomlist[Room] == 0:
            B_room = Room
            break
    print("Reserved room: ", B_room)
    name = input("Enter name of the guest: ")
    contact = str(input("Enter the contact: "))
    date = input
    print("""
    Reserved room \t:  {0}
    Name of guest \t:  {1}
    Contact \t\t:  {2}
    """.format(B_room,name,contact))
    ans = int(input("Enter '1' to confirm, '0' to reenter the info: "))
    if ans:                                     # if confirm, return the entered information, and today date
        Today = str(datetime.date.today())
        return B_room,name,contact,Today
    elif not ans:                               # if no, back to this func again to reenter
        CHECKin(room_type)


def recording(rooms, name, contact, date):
    """
        -> Write the data from CHECK _IN to file (guest_info.txt)
        -> Generate random number/string be ref_no
    """
    import random                               # to generate random ref_no
    import string                               # to create the string for randomize

    letters = string.ascii_uppercase
    digits = string.digits
    g = database.guest()                        # read from guestfile
    guestlist =g.guestlist

    def generate_ref_no(ref="1"):               # function to generate ref_no
        for i in range(3):
            ref+=random.choice(letters)
        for i in range(4):
            ref+=random.choice(digits)
        for i in range(len(guestlist)):
            if guestlist[i]["ref_no"]== ref :   # the generated ref_no is repeated
                ref = generate_ref_no()         # generate new ref_no
        return ref
    ref = generate_ref_no()

    # create new guest
    newGuest = {"ref_no":ref,"booking room":rooms,"name":name,"contact":contact,"checkin date": date}
    template = ["checkout date","food","beverage","service","sum"]
    for i in template:
        newGuest[i] = 0                         # put 0 temporarily
    g.updates(newGuest)                         # store the guest info into file

    r = database.room()
    r.updates(rooms,1)                          # then, update the room status
    print("Recorded successful")


def RECORDING():
    """
    @Nabil
        -> Any new bills (food & drinks & services) {RECORDING()}
        -> Based on the price (using tuple)
        -> Write to record_bill.txt
    """
    #READ file
    g = database.guest()
    listing =g.guestlist
    def checking_ref_no(ref,checks=False):      # to check either the ref_no is valide or not
        for i in range(len(listing)):
            if listing[i]["ref_no"]== ref :
                checks=True
        return checks
    ref_no = input("Please enter the ref_no: ")
    while not checking_ref_no(ref_no):
        print("Invalid ref_no, please enter again")
        ref_no = input("Please enter the ref_no: ")
    beverage = ["Ice cream","Orange juice","Apple juice"]
    food = ["Aglio olio","Chicken rice","Chicken Chop"]
    service = ["Dry cleaning","Car Rental","Guided tours"]
    order = []
    order_price = []
    sum_food = 0
    sum_beverage = 0
    sum_service = 0
    total_len = len(food) + len(beverage) + len(service)
    beverage_price = (2,1.5,2.5)                 # Tuple, the price is immutable
    food_price = (11.8,7.5,13.5)
    service_price = (20,75,35)
    print("---------- MENU ---------")           # Printing MENU
    print ("Code  Beverage      Price")
    print ("-------------------------")
    x = 1
    txt = '{:<6}{:<12}  {: >.2f}'
    for i in beverage:
        print (txt.format(x,i,beverage_price[x-1]))
        x+=1
    print ("")
    print ("Code  Food          Price")
    print ("-------------------------")
    for i in food:
        print (txt.format(x,i,food_price[x-len(beverage_price)-1]))
        x+=1
    print ("")
    print ("Code  Service       Price")
    print ("-------------------------")
    for i in service:
        print (txt.format(x,i,service_price[x-len(food_price)-len(beverage_price)-1]))
        x+=1
    print ("\nEnter the code to order.")
    print ("To end the order, please enter 0:")
    code = int(input ())
    while code != 0:
        if code > total_len or code < 0:
            print ("Invalid code!")
        elif code > 0 and code <= len(beverage):
            order.append(beverage[code-1])
            order_price.append(beverage_price[code-1])
            sum_beverage += beverage_price[code-1]
        elif code > len(beverage) and code <= len(beverage+food):
            order.append(food[code-len(beverage)-1])
            order_price.append(food_price[code-len(beverage_price)-1])
            sum_food += food_price[code-len(beverage_price)-1]
        elif code > len(beverage+food) and code <= total_len:
            order.append(service[code-len(food_price)-len(beverage_price)-1])
            order_price.append(service_price[code-len(food_price)-len(beverage_price)-1])
            sum_service += service_price[code-len(food_price)-len(beverage_price)-1]
        elif code == 0:
            break
        code = int(input ())
    print ("End of order!")
    total = 0
    for i in order_price:
        total += i                              # to calculate the sum
    print ("")
    print ("Ordered menu:")
    txt3 = '{:>12}{:>7.1f}'
    print ("   Ordered     Price")
    for i,j in zip(order,order_price):
        print (txt3.format(i,j))
    for Guest in listing:                       # to store new info about f&b
        if Guest["ref_no"]==ref_no:
            Guest["food"]+=sum_food             # record the new bill
            Guest["beverage"]+=sum_beverage
            Guest["service"]+=sum_service

    guestAfile = open("guest_info.txt","w")     # write to file
    for i in range(len(listing)):
        result = json.dumps(listing[i])
        guestAfile.write(result)                # write a new dict into file
        guestAfile.write("\n")
    guestAfile.close()
    print("The total price of F&B is RM {0:.2f}, and recorded successful".format(total))
    MENU()                                      # back to menu


def PRINT_OUT():
    """
    @Zul
        -> Receipt for checkout (ovewrite receipt.txt)
        -> Read from (guest's name & bills after check_out) and write to file
    """
    layout = """
********************************************
*          RECEIPT [ GSIX HOTEL ]          *
********************************************
* Name    : {0:20}           *
* Contact : {1:13}                  *
* Room    : {2:4}                           *
* Check-in  date : {3:10}              *
* Check-out date : {4:10}              *
********************************************
* Bill details                             *
* Food      :        RM {5:6.2f}             *
* Beverages :        RM {6:6.2f}             *
* Services  :        RM {7:6.2f}             *
* Room      :        RM {8:6.2f}             *
*------------------------------------------*
* Total     :        RM {9:6.2f}             *
*------------------------------------------*
*                                          *
*     THANK YOU AND WELCOME NEXT VISIT     *
********************************************
        """                                         # string formatting
    g = database.guest()
    def checking_ref_no(ref,checks=False):
        for i in range(len(g.guestlist)):
            if g.guestlist[i]["ref_no"]== ref :     # to check either the ref_no is valide or not
                checks=True
        return checks
    ref = input("Please enter the ref_no to print out: ")
    while not checking_ref_no(ref):
        print("Invalid ref_no, please enter again")
        ref = input("Please enter the ref_no: ")

    guestinfo = []
    for i in range(len(g.guestlist)):
        if g.guestlist[i]["ref_no"]== ref :         # invalid ref_no
            guestinfo =g.guestlist[i]

    name= guestinfo["name"]
    contact=guestinfo["contact"]
    room=guestinfo["booking room"]
    check_in=guestinfo["checkin date"]
    check_out=guestinfo["checkout date"]
    food=guestinfo["food"]
    beverages=guestinfo["beverage"]
    service=guestinfo["service"]
    room_price=guestinfo["sum"]-food-beverages-service
    total=guestinfo["sum"]
    receiptfile = open("receipt.txt","w")
    receiptfile.write(layout.format(name,contact,room,check_in,check_out,food,beverages,service,room_price,total))
    receiptfile.close()
    print("Receipt is printed out!")
    MENU()                                         # back to menu

def CHECK_OUT():
    """
    @Hanyi
        -> Record daytime (for check out)
        -> Calculate (sum & discount) (from daytime: check in to check out)
        -> Renew the room status
    """
    rstatus = ""
    food = 0
    beverage = 0
    service = 0
    total = 0
    outdate = datetime.date.today()
    outday = str(outdate)                          # record daytime (for check out)
    g = database.guest()
    def checking_ref_no(ref,checks=False):
        for i in range(len(g.guestlist)):
            if g.guestlist[i]["ref_no"]== ref :    # to check either the ref_no is valide or not
                checks = True
        return checks
    ref = input("Please enter your reference number: ")
    while not checking_ref_no(ref):
        print("Invalid ref_no, please enter again")
        ref = input("Please enter the ref_no: ")
    added = open("guest_info.txt","w")
    for i in range(len(g.guestlist)):
        if g.guestlist[i]["ref_no"]== ref :
            rstatus = g.guestlist[i]["booking room"]
            food = g.guestlist[i]["food"]
            beverage = g.guestlist[i]["beverage"]
            service = g.guestlist[i]["service"]
            print("This is the checkout for the Room",rstatus,"\nfood: ",food,"\nbeverage: ",beverage, "\nservice: ",service)
            #datetime calculation
            indate = datetime.date.fromisoformat(g.guestlist[i]["checkin date"])
            day = (outdate - indate).days
            if g.guestlist[i]["booking room"][0]== "A":
                total = food + beverage + service + 250*day       # calculate the sum
                g.guestlist[i]["sum"]= total                      # insert for the sum
                g.guestlist[i]["checkout date"]= outday           # record daytime
                print("Updated")
                print("The total bill is : ", total)
            elif g.guestlist[i]["booking room"][0]== "B":
                total = food + beverage + service + 200*day       # calculate the sum
                g.guestlist[i]["sum"]= total                      # insert for the sum
                g.guestlist[i]["checkout date"]= outday           # record daytime
                print("Updated")
                print("The total for bill is : ", total)
            elif g.guestlist[i]["booking room"][0]== "C":
                total = food + beverage + service + 150*day       # calculate the sum
                g.guestlist[i]["sum"]= total                      # insert for the sum
                g.guestlist[i]["checkout date"]= outday           # record daytime
                print("Updated")
                print("The total for bill is : ", total)
        result = json.dumps(g.guestlist[i])
        added.write(result)  #updated
        added.write("\n")
    added.close()

    r = database.room()
    r.updates(room_name=rstatus,func=0)                           # update room status
    print("Checked out successful, thank you.")
    MENU()                                                        # back to menu

MENU()

closing.bye()