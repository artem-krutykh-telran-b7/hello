import random

def exists(numbers, num):
    i = 0
    while i < len(numbers) and numbers[i] != num:
        i = i + 1
    return i < len(numbers)

def distinct_random_numbers(min, max, size):
    res = []
    if size <= max - min + 1:
        count = 0
        while count < size:
            num = random.randint(min, max)
            if not exists(res, num):
                res.append(num)
                count = count + 1
        return res


print(distinct_random_numbers(1, 49, 7))
