from random import randint

def max_sequence(seq):
    """
    Функция ищет пять соседних элементов списка, сумма значений которых максимальна.
    
    >>> max_sequence([1, 3, 1, 1, 4, 4, 3, 1, 4, 4, 4, 3, 4, 4, 1, 3, 2, 4, 4, 4])
    [4, 4, 4, 3, 4]
    
    >>> max_sequence([1, 5, 7, 2, 9, 2, 9, 2, 5, 3, 7, 6, 3, 3, 7, 4, 4, 1, 9, 5])
    [7, 2, 9, 2, 9]
    """   
    splittedNumbers = [seq[i:i+5] for i in range(0, len(seq)-4)]
    sums = list(map(sum, splittedNumbers))
    indexOfMaxSum = sums.index(max(sums))
    return splittedNumbers[indexOfMaxSum]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
