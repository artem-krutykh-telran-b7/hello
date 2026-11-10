def max_with_negative_duplicate(numbers: list[int]) -> int:
    seen: set[int] = set()
    largest_pair = 0
    for number in numbers:
        if number != 0 and -number in seen:
            largest_pair = max(largest_pair, abs(number))
        seen.add(number)
    return largest_pair if largest_pair else -1


def sumOfTwoExists(numbers: list[int], sum: int) -> bool:
    seen: set[int] = set()
    for number in numbers:
        if sum - number in seen:
            return True
        seen.add(number)
    return False


def _move_max_to_end(numbers: list[int], end: int) -> bool:
    swapped = False
    for index in range(end):
        if numbers[index] > numbers[index + 1]:
            numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
            swapped = True
    return swapped


def bubble_sort(numbers: list[int]) -> None:
    end = len(numbers) - 1
    while end > 0 and _move_max_to_end(numbers, end):
        end -= 1


def remove_duplicates(numbers: list[int]) -> list[int]:
    seen: set[int] = set()
    unique_numbers = []
    for number in numbers:
        if number not in seen:
            seen.add(number)
            unique_numbers.append(number)
    return unique_numbers
