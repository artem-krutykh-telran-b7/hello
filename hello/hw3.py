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