from typing import Callable, Sequence


def __move_max_to_end(
    items: list[object],
    end: int,
    key: Callable[[object], object] | None = None,
) -> int:
    swaps = 0
    for index in range(end):
        left = items[index]
        right = items[index + 1]
        if key is not None:
            left = key(left)
            right = key(right)
        if right < left:
            items[index], items[index + 1] = items[index + 1], items[index]
            swaps += 1
    return swaps


def bubble_sorted(
    items: Sequence[object],
    key: Callable[[object], object] | None = None,
) -> list[object]:
    result: list[object] = list(items)
    end = len(result) - 1
    while end > 0 and __move_max_to_end(result, end, key) > 0:
        end -= 1
    return result


def even_asc_odd_desc(numbers: list[int]) -> list[int]:
    return sorted(
        numbers,
        key=lambda number: (number % 2, number if number % 2 == 0 else -number),
    )


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