from math import sqrt

testlist = [2, 4, 9, 16, 25]

newlist1 = []
for i in [2, 4, 9, 16, 25]:
    newlist1.append(sqrt(i))
print(newlist1)

newlist2 = []
newlist2 = list(map(sqrt, testlist))
print(newlist2)

newlist3 = [sqrt(i) for i in testlist]
print(newlist3)
