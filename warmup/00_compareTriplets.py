#_*_ coding: utf-8 _*_
#test data
alice = [5, 6, 7]
bob = [3, 6, 10]

def compareTriplets(a, b):
    #define container for results
    alicePoints = []
    bobPoints = []
    pointsTied = []
    #how to prevent if list do not have same length
    #Get the index value of list
    for i in range(len(a)): 
        #if statement decide whom get point
        if a[i] > b[i]:
#            print("Point To Alice")
            alicePoints.append(1)
        elif a[i] < b[i]:
#            print ("Point to Bob")
            bobPoints.append(1)
        else:
#            print("Tied!")
            pointsTied.append(1)
    #combine value to return single array
    finalScore = [sum(alicePoints) ,sum(bobPoints)]
    return finalScore
compareTriplets(alice,bob)