import hw10
import unittest_print


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
unittest_print.print_test(
    "all range",
    [3, 4, 5, 6, 7, 8, 9],
    hw10.get_all_range(numbers, range(3, 10)),
)
unittest_print.print_test("empty range", [], hw10.get_all_range(numbers, range(5, 5)))
unittest_print.print_test("missing allowed", numbers, hw10.get_all_range(numbers))

unittest_print.print_test(
    "not in range",
    [1, 2, 8, 9, 10],
    hw10.get_all_not_in_range(numbers, range(3, 8)),
)
unittest_print.print_test(
    "empty disallowed range",
    numbers,
    hw10.get_all_not_in_range(numbers, range(5, 5)),
)
unittest_print.print_test(
    "stepped range",
    [3, 5, 7, 9],
    hw10.get_all_range(numbers, range(3, 10, 2)),
)
unittest_print.print_test(
    "descending range",
    [4, 6, 8],
    hw10.get_all_range(numbers, range(8, 2, -2)),
)
unittest_print.print_test(
    "values outside stepped range",
    [1, 2, 4, 6, 8, 10],
    hw10.get_all_not_in_range(numbers, range(3, 10, 2)),
)

unittest_print.print_test(
    "sort numbers",
    [-11, -3, 0, 2, 4, 7, 10],
    hw10.my_sorted([-3, 10, 7, 0, 4, -11, 2]),
)
unittest_print.print_test(
    "sort tuple",
    [1, 2, 3],
    hw10.my_sorted((3, 1, 2)),
)
unittest_print.print_test(
    "sort key",
    [0, 2, -3, 4, 7, 10, -11],
    hw10.my_sorted([-3, 10, 7, 0, 4, -11, 2], key=abs),
)
unittest_print.print_test(
    "sort strings by length",
    ["x", "bb", "aaa", "cccc"],
    hw10.my_sorted(["cccc", "x", "aaa", "bb"], key=len),
)

unittest_print.print_results()
