from random import randint

def num_input():
    x = int(input("Enter number between 0 & 36... "))
    return x

x = num_input() 
# x = 0 # last number on the Roulette table
y = randint(0,36)

gohigh = 0
golow = 0
xyerror = 0

count = 0
turns = 1

red = ["1", "3", "5", "7", "9", "12", "14", "16", "18", "19", "21", "23", "25", "27", "30", "32", "34", "36"]
black = ["2", "4", "6", "8", "10", "11", "13", "15", "17", "20", "22", "24", "26", "28", "29", "31", "33", "35"]
green = ["0"]

Ccolour = "unknown"
Ncolour = "unknown"

while count < turns:
#    f = open("output.txt", "a") # output a text file for results

    if str(x) in red:
        Ccolour = "Red"
    elif str(x) in black:
        Ccolour = "Black"
    elif str(x) in green:
        Ccolour = "Green"
    else:
        print("Error setting current colour!")

    if str(y) in red:
        Ncolour = "Red"
    elif str(y) in black:
        Ncolour = "Black"
    elif str(y) in green:
        Ncolour = "Green"
    else:
        print("Error setting new colour!")

    if x > y and x != 0:
#        f.write("Go lower! Last number was " + str(x) + ", random number was " + str(y) + ". \n") 
        print("Go lower! Last number was " + str(Ccolour) + " " + str(x) + ", random number is " + str(Ncolour) + " " + str(y) + ". \n") 
        golow += 1
    elif x < y and x != 0:
 #       f.write("Go higher! Last number was " + str(x) + ", random number was " + str(y) + ". \n")
        print("Go higher! Last number was " + str(Ccolour) + " " + str(x) + ", random number is " + str(Ncolour) + " " + str(y) + ". \n") 
        gohigh += 1
    elif x == 0:
 #       f.write("Go higher! Last number was " + str(x) + ", random number was " + str(y) + ". \n")
        print("Go higher! Last number was " + str(Ccolour) + " " + str(x) + ", random number is " + str(Ncolour) + " " + str(y) + ". \n")  
        gohigh += 1
    elif x == 36:
 #       f.write("Go lower! Last number was " + str(x) + ", random number was " + str(y) + ". \n")
        print("Go lower! Last number was " + str(Ccolour) + " " + str(x) + ", random number is " + str(Ncolour) + " " + str(y) + ". \n") 
        golow += 1
    else: 
 #       f.write("Error? " + str(x) + "  "+ str(y) + "\n")
        print("Error? " + str(x) + " "+ str(y) + ". \n")
        xyerror += 1
    count += 1

print('Turns played: ' + str(count))
print(str(gohigh) + ' Gone High')
print(str(golow) + ' Gone Low')

# f.write('Turns played: ' + str(count) + "\n")
# f.write(str(gohigh) + ' Gone High' + "\n")
# f.write(str(golow) + ' Gone Low' + "\n")

input()
