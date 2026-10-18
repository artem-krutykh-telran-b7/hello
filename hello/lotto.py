import random

def exists(numbers, num):
    for n in numbers:
        if n == num:
            return True
    return False

def distinct_random_numbers(min, max, size):
    res = []
    if size > max - min + 1:
        return res
    count = 0
    while count < size:
        num = random.randint(min, max)
        if not exists(res, num):
            res.append(num)
            count = count + 1
    return res
print(distinct_random_numbers(1, 49, 7))