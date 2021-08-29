# coding=UTF-8
from random import *
import math
from time import process_time
RSALIST = "25195908475657893494027183240048398571429282126204032027777137836043662020707595556264018525880784406918290641249515082189298559149176184502808489120072844992687392807287776735971418347270261896375014971824691165077613379859095700097330459748808428401797429100642458691817195118746121515172654632282216869987549182422433637259085141865462043576798423387184774447920739934236584823824281198163815010674810451660377306056201619676256133844143603833904414952634432190114657544454178424020924616515723350778707749817125772467962926386356373289912154831438167899885040445364023527381951378636564391212010397122822120720357"
RSA_2048= int(RSALIST)

#SINCE ITS DIVISIBLE BY 2, IS DIVISIBLE BY 4 , 6 , 8?
#check odd and even
factors = []

def getFactorsUsingParity(dividend):
    start = process_time()
    factors = []
    print("Started at "+str(start))

    if dividend % 2 != 0:
        #number is odd
        #so odd*odd*odd

def getFactors(dividend):
    start = process_time()
    twentyFourBits = 0xffffff
    factors=[]
    divisor=2
    print("Started at "+str(start))
    iterations=0
    while dividend != divisor or len(factors) > 2:
        iterations+=1
        divisor = 2
        temp = dividend % divisor
        if temp != 0:
            divisorT = divisor
            remainder  = dividend % divisorT
            while remainder != 0 :
                iterations+=1
                remainder = dividend % divisorT
                divisorT+=1
                iterations += 1
                if iterations % 3000000 == 0:
                    print("[Dividend] " + str(dividend) + " [Divisor] "+str(divisorT),end = " ")
                    print("[Remainder] "+str(remainder))
                    iterations=0


            factors.append(divisorT)
            divisor=divisorT

        else:
            factors.append(divisor)

        dividend = dividend / divisor





    endTime =process_time()
    print("ELAPSED TIME "+str(endTime-start))
    factors.append(dividend)
    return factors

#RSA Laboratories states that: for each RSA number n, there exists prime numbers p and q such that
#   n = p × q.
#
#The problem is to find these two primes, given only n.


#RSA_2048 = readRSALists()
key = int(RSA_2048)
factors = getFactors(key)
print(str(factors))
