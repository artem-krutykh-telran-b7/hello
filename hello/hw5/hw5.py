def minMaxAverage(numbers: list[int]) -> tuple[int, int, float]:
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0
    for n in numbers:
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n
        total += n
    average = total / len(numbers)
    return minimum, maximum, average

def moveMaxToEnd(numbers: list[int]) -> None:
    max_index = 0
    for i, n in enumerate(numbers):
        if n > numbers[max_index]:
            max_index = i
    while max_index < len(numbers) - 1:
        numbers[max_index], numbers[max_index + 1] = numbers[max_index + 1], numbers[max_index]
        max_index += 1