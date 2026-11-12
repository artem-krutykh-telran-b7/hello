def max_with_negative_duplicate(numbers: list[int]) -> int:
    seen: set[int] = set()
    largest_pair = 0
    for number in numbers:
        if abs(number) > largest_pair:
            if -number in seen:
                largest_pair = abs(number)
            else:
                seen.add(number)
    return largest_pair if largest_pair else -1


def sumOfTwoExists(numbers: list[int], sum: int) -> bool:
    seen: set[int] = set()
    index = 0
    while index < len(numbers) and numbers[index] not in seen:
        seen.add(sum - numbers[index])
        index += 1
    return index < len(numbers)


def _move_max_to_end(numbers: list[int], end: int) -> bool:
    swapped = False
    for index in range(end):
        if numbers[index] > numbers[index + 1]:
            numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
            swapped = True
    return swapped


def bubble_sort(numbers: list[int]) -> None:
    end = len(numbers) - 1
    while _move_max_to_end(numbers, end):
        end -= 1


def remove_duplicates(numbers: list[int]) -> list[int]:
    seen: set[int] = set()
    return [number for number in numbers if number not in seen and not seen.add(number)]
