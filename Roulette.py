from random import randint

x = 0 # last number on the Roulette table
y = randint(0,36)

gohigh = 0
golow = 0
xyerror = 0

count = 0
turns = 1

while count < turns:
    f = open("output.txt", "a")
    if x > y and x != 0:
        f.write("Go lower! Last number was " + str(x) + ", random number was " + str(y) + ". \n") 
        print("Go lower! Last number was " + str(x) + ", random number was " + str(y) + ". \n") 
        golow += 1
    elif x < y and x != 0:
        f.write("Go higher! Last number was " + str(x) + ", random number was " + str(y) + ". \n")
        print("Go higher! Last number was " + str(x) + ", random number was " + str(y) + ". \n") 
        gohigh += 1
    elif x == 0:
        f.write("Go higher! Last number was " + str(x) + ", random number was " + str(y) + ". \n")
        print("Go higher! Last number was " + str(x) + ", random number was " + str(y) + ". \n") 
        gohigh += 1
    elif x == 36:
        f.write("Go lower! Last number was " + str(x) + ", random number was " + str(y) + ". \n")
        print("Go lower! Last number was " + str(x) + ", random number was " + str(y) + ". \n") 
        golow += 1
    else: 
        f.write("Error? " + str(x) + "  "+ str(y) + "\n")
        print("Error? " + str(x) + "  "+ str(y) + "\n")
        xyerror += 1
#    x = y
#    y = randint(0,36)
    count += 1

print('Turns played: ' + str(count))
print(str(gohigh) + ' Gone High')
print(str(golow) + ' Gone Low')

f.write('Turns played: ' + str(count) + "\n")
f.write(str(gohigh) + ' Gone High' + "\n")
f.write(str(golow) + ' Gone Low' + "\n")

input()
