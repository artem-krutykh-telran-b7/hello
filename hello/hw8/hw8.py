from typing import Callable, Sequence

def bubble_sorted(
    items: Sequence[object],
    key: Callable[[object], object] | None = None,
) -> list[object]:
    result: list[object] = list(items)
    for end in range(len(result) - 1, 0, -1):
        for index in range(end):
            left = result[index]
            right = result[index + 1]
            if key is not None:
                left = key(left)
                right = key(right)
            if right < left:
                result[index], result[index + 1] = result[index + 1], result[index]
    return result

def even_asc_odd_desc(numbers: list[int]) -> list[int]:
    even_numbers = [n for n in numbers if n % 2 == 0]
    odd_numbers = [n for n in numbers if n % 2 != 0]
    even_sorted = bubble_sorted(even_numbers)
    odd_sorted = bubble_sorted(odd_numbers, lambda n: -n)
    return even_sorted + odd_sorted

def merge(
    part1: Sequence[object],
    part2: Sequence[object],
    key: Callable[[object], object] | None = None,
) -> list[object]:
    result: list[object] = []
    i = 0
    j = 0
    while i < len(part1) and j < len(part2):
        left = part1[i]
        right = part2[j]
        if key is not None:
            left = key(left)
            right = key(right)
        if right < left:
            result.append(part2[j])
            j += 1
        else:
            result.append(part1[i])
            i += 1
    for item in part1[i:]:
        result.append(item)
    for item in part2[j:]:
        result.append(item)
    return result