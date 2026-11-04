def int_reverse(num):
    return str(num)[::-1]

def create_palindromic_list(start, stop):
    step = 1 if start <= stop else -1
    return [num for num in range(start, stop + step, step) if str(num) == int_reverse(num)]

print(create_palindromic_list(20,40))

print(create_palindromic_list(40, 20))