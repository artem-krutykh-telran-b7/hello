from typing import Callable


def merge_in_place[T](
    items: list[T],
    start: int,
    len1: int,
    size: int,
    key: Callable[[T], T] | None = None,
) -> None:
    """Merge two sorted parts in place using O(1) extra space.

    The worst-case running time is O(N^2), since elements may need to be
    shifted one position at a time.
    """
    first = start
    second = start + len1
    end = start + size

    while first < second and second < end:
        left = items[first]
        right = items[second]
        left_key = key(left) if key is not None else left
        right_key = key(right) if key is not None else right

        if right_key < left_key:
            item = items[second]
            index = second
            while index > first:
                items[index] = items[index - 1]
                index -= 1
            items[first] = item
            first += 1
            second += 1
        else:
            first += 1
