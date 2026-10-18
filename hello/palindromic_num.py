def int_reverse(num):
    res = str(num % 10)
    num = num // 10
    while num != 0:
        res = res + str(num % 10)
        num = num // 10
    return res

def create_palindromic_list(start, stop):
    res = []
    step = 1
    if start > stop:
        step = -1
    for num in range(start, stop + step, step):
        if int_reverse(num) ==str(num):
            res.append(num)
    return res

print(create_palindromic_list(20,40))

print(create_palindromic_list(40, 20))