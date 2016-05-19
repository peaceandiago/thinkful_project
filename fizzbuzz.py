import sys 

numCount = None

while not numCount:
    try:
        numCount = int(sys.argv[1])
    except IndexError:
        numCount = int(input("Well you need to put some digits  "))
    except NameError:
        numCount = int(input("C'mon now we need a number"))
    except ValueError:
        try:
            numCount = int(input("Tsk, not a letter, a number  "))  
        except:
            continue

def fizzBuzz(n):
    
    for n in range (1, n + 1):
        if n % 3 == 0 and n % 5 == 0:
            print ("Fizzbuzz") 
        elif n % 3 == 0:
            print ("Fizz") 
        elif n % 5 == 0: 
            print ("Buzz") 
        else:
            print (n)

fizzBuzz(numCount)
fizzBuzz(10)









