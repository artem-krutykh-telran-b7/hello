from typing import Callable, Sequence


def __merge[T, K](
    part1: list[T],
    part2: list[T],
    key: Callable[[T], T | K],
) -> list[T]:
    index1 = 0
    index2 = 0
    len1 = len(part1)
    len2 = len(part2)
    result: list[T] = []

    while index1 < len1 and index2 < len2:
        if key(part1[index1]) <= key(part2[index2]):  # pyright: ignore[reportOperatorIssue]
            result.append(part1[index1])
            index1 += 1
        else:
            result.append(part2[index2])
            index2 += 1

    result.extend(part1[index1:])
    result.extend(part2[index2:])
    return result


def __get_sorted_part[T, K](
    items: Sequence[T],
    start: int,
    key: Callable[[T], T | K],
) -> list[T]:
    result = [items[start]]
    last = len(items) - 1

    while start < last and key(items[start]) <= key(items[start + 1]):  # pyright: ignore[reportOperatorIssue]
        start += 1
        result.append(items[start])

    return result


def __get_sorted_parts[T, K](
    items: Sequence[T],
    key: Callable[[T], T | K],
) -> list[list[T]]:
    result: list[list[T]] = []
    start = 0
    size = len(items)

    while start < size:
        part = __get_sorted_part(items, start, key)
        result.append(part)
        start += len(part)

    return result


def __merge_in_pairs[T, K](
    sorted_parts: list[list[T]],
    key: Callable[[T], T | K],
) -> list[list[T]]:
    result: list[list[T]] = []
    index = 0

    while index + 1 < len(sorted_parts):
        result.append(__merge(sorted_parts[index], sorted_parts[index + 1], key))
        index += 2

    if index < len(sorted_parts):
        result.append(sorted_parts[index])

    return result


def __merge_parts[T, K](
    sorted_parts: list[list[T]],
    key: Callable[[T], T | K],
) -> list[T]:
    while len(sorted_parts) > 1:
        sorted_parts = __merge_in_pairs(sorted_parts, key)

    result: list[T] = []
    if len(sorted_parts) == 1:
        result = sorted_parts[0]

    return result


def my_sorted[T, K](
    items: Sequence[T],
    /,
    *,
    key: Callable[[T], T | K] | None = None,
) -> list[T]:
    if key is None:
        key = lambda item: item

    sorted_parts = __get_sorted_parts(items, key)
    result = __merge_parts(sorted_parts, key)
    return result
