#_*_ coding: utf-8 _*_
#test data
# out put number of pairs
nIn = 9
arIn = [10, 20, 20, 10, 10, 30, 50, 10, 20]
#result should be 3

def sockMerchant(n, ar):
    #create value container
    tally = []
    leftSock = []
    #Loop through list till 0
    while (len(ar) > 0):
        #define last index in list
        value = ar[-1]
        #remove last index in list
        ar.pop()
        #find the other pair in list
        if value in ar:
            ar.remove(value)
            tally.append(1)
        else:
            leftSock.append(1)
    print(sum(tally))
    return sum(tally)



sockMerchant (nIn, arIn)