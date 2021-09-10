

def add(num,begin,end):
    for summand in range(begin,end):
        sum = summand
        block=0
        print(" SUMMAND "+str(sum))
        while sum < num:
            block+=1
            sum+=summand
            print(str(sum))
        if sum==num :
            block+=1
            print("GO IT "+str(block)+" "+str(sum))
            input("PRESS")
            return
        print("SUM "+str(sum)+" large "+str(num) +" Doesnt divide")

# BEGIN MUST BE > 1
add(1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139,23553515235251246213515135155342235232352255226422,3535553512342352352532255235232533553121422642462612124124152313)















































































































































