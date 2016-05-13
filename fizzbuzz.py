import sys 

try:
   numCount = int(sys.argv[1])
except IndexError:
    numCount = int(input("Well you need to put some digits  "))
except NameError:
    numCount = int(input("C'mon now we need a number"))
except ValueError:
    numCount = int(input("Tsk, not a letter, a number  "))   


for numCount in range (1, numCount + 1):
    if numCount % 3 == 0 and numCount % 5 == 0:
        print ("Fizzbuzz") 
    elif numCount % 3 == 0:
        print ("Fizz") 
    elif numCount % 5 == 0: 
        print ("Buzz") 
    else:
        print (numCount)


