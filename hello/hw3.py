def indexOf(numbers, num):
    i = 0
    while i < len(numbers) and numbers[i] != num:
        i += 1
    return i if i < len(numbers) else -1

def lastIndexOf(numbers, num):
    i = len(numbers) - 1
    while i >= 0 and numbers[i] != num:
        i -= 1
    return i

def min_even(numbers):
    evens = [x for x in numbers if x % 2 == 0]
    res = evens[0]
    for x in evens:
        if x < res:
            res = x
    return res

def count(numbers, num):
    return len([x for x in numbers if x == num])

