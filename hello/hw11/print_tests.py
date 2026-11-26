from random import randint

import hw11
import unittest_print


items = [20, -10, 1, 30, -11, 1, -50]
unittest_print.print_test("empty list", [], hw11.my_sorted([]))
unittest_print.print_test("single item", [3], hw11.my_sorted([3]))
unittest_print.print_test(
    "already sorted runs",
    [-10, -3, 1, 20, 25, 30, 40, 41],
    hw11.my_sorted([-10, -3, 1, 20, 25, 30, 40, 41]),
)
unittest_print.print_test(
    "several sorted runs",
    [-50, -11, -10, 1, 1, 20, 30],
    hw11.my_sorted(items),
)
unittest_print.print_test(
    "reverse sorted input",
    [1, 2, 3, 4, 5],
    hw11.my_sorted([5, 4, 3, 2, 1]),
)
unittest_print.print_test(
    "sort by key",
    sorted(items, key=lambda item: str(item)),
    hw11.my_sorted(items, key=lambda item: str(item)),
)
unittest_print.print_test(
    "stable ordering for equal keys",
    [(1, "first"), (1, "second"), (2, "middle")],
    hw11.my_sorted(
        [(1, "first"), (2, "middle"), (1, "second")],
        key=lambda item: item[0],
    ),
)
unittest_print.print_test(
    "input is unchanged",
    [20, -10, 1, 30, -11, 1, -50],
    items,
)

random_items = [randint(1, 100000) for _ in range(1022)]
sorted_random_items = hw11.my_sorted(random_items)
unittest_print.print_test(
    "random values",
    True,
    sorted_random_items == sorted(random_items),
)
sorted_random_items_by_str = hw11.my_sorted(random_items, key=lambda item: str(item))
unittest_print.print_test(
    "random values by string key",
    True,
    sorted_random_items_by_str == sorted(random_items, key=lambda item: str(item)),
)

unittest_print.print_results()
