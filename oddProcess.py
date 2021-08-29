
from time import process_time

RSALIST = "25195908475657893494027183240048398571429282126204032027777137836043662020707595556264018525880784406918290641249515082189298559149176184502808489120072844992687392807287776735971418347270261896375014971824691165077613379859095700097330459748808428401797429100642458691817195118746121515172654632282216869987549182422433637259085141865462043576798423387184774447920739934236584823824281198163815010674810451660377306056201619676256133844143603833904414952634432190114657544454178424020924616515723350778707749817125772467962926386356373289912154831438167899885040445364023527381951378636564391212010397122822120720357"
RSA_2048= int(RSALIST)

#
#dividir varias vezes um numero => dividir apenas um numero composto pelos numeros anteriores
#
# 9^3 = 729 = {
#
# negate even = > 8=2*2+2 , odd = not even 8
#
#

obter factores do divisor, (2,4,8)

#are: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99.

def getFactorsOdds(dividend):
    start = process_time()
    factors = []
    print("Started at "+str(start))
    iterations = 0
    #dividend is odd (RSA2048 is odd)
    divisor = 1
    # se gcd for igual ao menor numero, entao é factor

    while dividend != divisor and len(factors) < 2:
        iterations += 1
        factors.append(divisor)
        divisor+=2
        remainder = dividend % divisor
        if remainder == 0:
            factors.append(divisor)
        else:
            divisorT = divisor
            remainderT = dividend % divisorT
            while remainderT != 0:
                iterations += 1
                remainderT = dividend % divisorT
                if iterations % 3000000 == 0:
                   print("Factor trying: " + str(divisorT) + " Rem " + str(remainderT))
                   print("[Dividend] " + str(dividend) + "\n[Divisor] " + str(divisorT), end=" ")
                   print("[Remainder] " + str(remainder)+"\n")
                   iterations = 0
                divisorT+=2
            factors.append(divisorT)
            #print(str(factors))
            divisor = divisorT
        dividend = dividend / divisor
    endTime = process_time()
    print("ELAPSED TIME " + str(endTime - start))
    factors.append(dividend)
    return factors



facs = getFactorsOdds(RSA_2048)
print(str(facs))

#def multiples(m, count):
#    for i in range(count):
#        print(str(i*m)+ " number "+str(i))

#multiples(6328,100)