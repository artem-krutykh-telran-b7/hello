from bisect import bisect_left
from math import sqrt
from typing import Callable, Sequence, cast


def get_all_range(numbers: Sequence[int], allowed: range | None = None) -> list[int]:
    result: list[int] = cast(list[int], numbers)

    if allowed is not None:
        result = []
        if len(allowed) > 0:
            lower = allowed[0]
            upper = allowed[-1]
            if lower > upper:
                lower, upper = upper, lower
            start = bisect_left(numbers, lower)
            end = bisect_left(numbers, upper)
            result = list(numbers[start:end])

    return result


def get_all_not_in_range(numbers: Sequence[int], disallowed: range) -> list[int]:
    return [number for number in numbers if number not in disallowed]


def __move_max_to_end[T, K](
    items: list[T],
    end: int,
    key: Callable[[T], T | K],
) -> int:
    swaps = 0
    for index in range(end):
        left = key(items[index])
        right = key(items[index + 1])
        if right < left:  # pyright: ignore[reportOperatorIssue]
            items[index], items[index + 1] = items[index + 1], items[index]
            swaps += 1
    return swaps


def __bubble_sorted[T, K](
    items: list[T],
    key: Callable[[T], T | K],
) -> list[T]:
    result = items
    end = len(result) - 1
    while end > 0 and __move_max_to_end(result, end, key) > 0:
        end -= 1
    return result


def __merge[T, K](
    part1: Sequence[T],
    part2: Sequence[T],
    key: Callable[[T], T | K],
) -> list[T]:
    result: list[T] = []
    index1 = 0
    index2 = 0

    while index1 < len(part1) and index2 < len(part2):
        left = part1[index1]
        right = part2[index2]
        if key(right) < key(left):  # pyright: ignore[reportOperatorIssue]
            result.append(right)
            index2 += 1
        else:
            result.append(left)
            index1 += 1

    result.extend(part1[index1:])
    result.extend(part2[index2:])
    return result


def my_sorted[T, K](
    items: Sequence[T],
    /,
    *,
    key: Callable[[T], T | K] | None = None,
) -> list[T]:
    if key is None:
        key = lambda item: item

    size = len(items)
    block_size = 1
    if size > 0:
        block_size = size // int(sqrt(size))
    blocks: list[list[T]] = []
    start = 0

    while start < size:
        end = start + block_size
        if end + block_size > size:
            end = size
        blocks.append(__bubble_sorted(list(items[start:end]), key))
        start = end

    result: list[T] = []
    if len(blocks) > 0:
        result = blocks[0]
        index = 1
        while index < len(blocks):
            result = __merge(result, blocks[index], key)
            index += 1

    return result
