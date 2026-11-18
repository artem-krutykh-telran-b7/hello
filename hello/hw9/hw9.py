from typing import Callable


def __move_item_to_index[T](items: list[T], source: int, destination: int) -> None:
    item = items[source]
    index = source
    while index > destination:
        items[index] = items[index - 1]
        index -= 1
    items[destination] = item


def merge_in_place[T](
    items: list[T],
    start: int,
    len1: int,
    size: int,
    key: Callable[[T], T] | None = None,
) -> None:
    first = start
    second = start + len1
    end = start + size

    while first < second and second < end:
        left = items[first]
        right = items[second]
        left_key = key(left) if key is not None else left
        right_key = key(right) if key is not None else right

        if right_key < left_key:
            __move_item_to_index(items, second, first)
            first += 1
            second += 1
        else:
            first += 1
