
#_*_ coding: utf-8 _*_
#test data
'''
Complete the countingValleys function in the editor below. 
It must return an integer that denotes the number of valleys Gary traversed. 
BONUS:
If we represent _ as sea level, a step up as /, and a step down as \,
'''
#n: the number of steps Gary takes 
nn = 8
#s: a string describing his path 
ss = ['U','D','D','D','U','D','U','U']
sss = ['U','U','D','D','U','D','U','U']
5


# Complete the countingValleys function below.
def countingValleys(n, s):
    #add a unit test case- for practice
    # variable to keep track of number of valley
    numOvalley = 0
    # vaiable for the valley pattern, 
    previousValue= 'D' #working things out to find the pattern
    #walk through list
    for path in s:
        #eveluate if the value is not equal to "D"
        if path != previousValue:
            #if meet requirement then add value
            numOvalley = numOvalley + 1
            print(f'Valley {numOvalley}')
            #need work since it only counts the nummber of "U"
            #add another requirement that looks at the previoud index 

    
countingValleys(nn,sss)
    
    
    
"""
help to solve problems..

Read the problem completely twice.
Solve the problem manually with 3 sets of sample data.
Optimize the manual steps.
Write the manual steps as comments or pseudo-code.
Replace the comments or pseudo-code with real code.
Optimize the real code.
"""