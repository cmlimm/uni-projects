from random import randint

numbers = [randint(-20, 20) for i in range(100)]

minimum = min(numbers)
maximum = max(numbers)

minIndex = numbers.index(minimum)
maxIndex = numbers.index(maximum)
numbers.reverse()
maxIndexReverse = -numbers.index(maximum)-1
minIndexReverse = -numbers.index(minimum)-1
numbers.reverse()

sublists = [numbers[minIndex:maxIndex+1],
            numbers[minIndex:maxIndexReverse+1],
            numbers[maxIndex:minIndex+1],
            numbers[maxIndex:minIndexReverse+1],
            numbers[minIndexReverse:maxIndex+1],
            numbers[minIndexReverse:maxIndexReverse+1],
            numbers[maxIndexReverse:minIndex+1],
            numbers[maxIndexReverse:minIndexReverse+1]]

lenOfSublists = list(map(len, sublists))
maxLenSublist = sublists[lenOfSublists.index(max(lenOfSublists))]

listOfNegative = [x for x in maxLenSublist if x<0]
print(len(listOfNegative))
