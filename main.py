from random import *
import math
#Tried number 6328.
#d = 6328 / 2
#d = 3164 / 2
#d = 1582 / 2
#d = 791 / 2  # doesnt divide
#d = 791 / 3  # nop another one
#     791 / 7
#     113 / prime

factors = []

def isPrime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def getFactores(dividend):

    while not isPrime(dividend):
        divisor = 2

        temp = dividend % divisor
        if temp != 0:
            divisorT = divisor
            tempAux  = dividend % divisorT
            while tempAux != 0 :
                divisorT += 1
                tempAux = dividend % divisorT
            factors.append(divisorT)
            divisor=divisorT

        else:
            factors.append(divisor)
        dividend = dividend / divisor
    factors.append(dividend)



def printList():
    total=1
    for ele in range(0, len(factors)):
        total = total * factors[ele]

    print("TOTAL "+str(total))

key = math.pow(2,995)
getFactores(key)
# prints the multiplications of all the elements of ao list
printList()