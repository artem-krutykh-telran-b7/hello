def binary_search(numbers: list[int], num: int) -> int:
    left = 0
    right = len(numbers)

    while left < right:
        middle = (left + right) // 2
        if numbers[middle] < num:
            left = middle + 1
        else:
            right = middle

    if left < len(numbers) and numbers[left] == num:
        return left
    return -(left + 1)


def insert_sorted(numbers: list[int], num: int) -> None:
    index = binary_search(numbers, num)
    if index < 0:
        index = -index - 1
    numbers.insert(index, num)
