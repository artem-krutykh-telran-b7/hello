def minMaxAverage(numbers: list[int]) -> tuple[int, int, float]:
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0
    for n in numbers:
        if n < minimum:
            minimum = n
        elif n > maximum:
            maximum = n
        total += n
    average = total / len(numbers)
    return minimum, maximum, average

def moveMaxToEnd(numbers: list[int]) -> None:
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]