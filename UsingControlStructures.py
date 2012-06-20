theInput = raw_input("Enter an integer: ")
#Your code here
theInput=int(theInput)
if theInput%2==0:
    print "even"
else:
    print "odd"

print "------------------------------------------------------"
primaryschoolAge=4
legalvotingAge=18
becomepresidentAge=30
retirementAge=60
personAge=input("Enter your age:")
if personAge<primaryschoolAge:
    print "too young"
elif personAge>=legalvotingAge:
    print "remember to vote"
if personAge>=becomepresidentAge:
    print"vote for me"
else :
    print "You can't be president"
    
if personAge>=retirementAge:
    print"Too old"








print "-------------------------------------------------------------"

i=40
while i>0:
    i=i-1
    if i%3==0:
        print i
    
