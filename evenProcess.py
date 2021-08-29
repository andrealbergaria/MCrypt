from time import process_time

#trying to get the following algorithm:
#instead of dividing by say 2,4, divide by 8, and we know that the dividend has 2,4
#To use the odd numbers, just negate the even numbers




def getFactorsEven(dividend):
    start = process_time()
    twentyFourBits = 0xffffff
    factors=[]
    divisor=2
    print("Started at "+str(start))
    iterations=0
    #dividen is even. Two possibilitesa even*even or even*odd

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
