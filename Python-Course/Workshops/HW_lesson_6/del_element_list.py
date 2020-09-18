names = ['John', 'Paul', 'George', 'Ringo']

filtNames = list(filter(lambda x: x == 'John' or x == 'Paul', names))
print(filtNames)
