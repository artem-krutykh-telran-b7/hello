def indexOf(numbers, num):
    i = 0
    while i < len(numbers) and numbers[i] != num:
        i += 1
    return i if i < len(numbers) else -1
