import datetime
x, y, i = input("Enter your name: "), input("Enter your age: "), 0

### CHECK THE NAME ###

while(i < len(x) and (('z' >= x[i] >= 'a') or ('Z' >= x[i] >= 'A'))):
    i += 1
 
if(i != len(x) or len(x) == 0):
    print("Your name must contain string")
    exit()


### CHECK THE AGE ###

try:
    y = int(y)
except ValueError:
    print("Please enter a valid number")
    exit()

if(y > 120)
    print("You either broke the world record or just being silly")
    exit()

if(y < 0):
    print("Please enter number bigger than zero")
    exit()


### CALCULATE AND PRINT ###

year = datetime.datetime.now().year
year100at = int(year) + (100 - y)

print("Hi", x, end='')

if(y < 100):
    print(", your will turn 100 in the year", year100at)
    exit()
else:
    print(", you alread turned 100 at the year", year100at)

