import hw8
import unittest_print

numbers = [-2, -10, 12, 3, -22, 6, 21, 5, 4]
sorted_numbers = [-22, -10, -2, 3, 4, 5, 6, 12, 21]
sorted_numbers_abs = [-2, 3, 4, 5, 6, -10, 12, 21, -22]
sorted_even_odd = [-22, -10, -2, 4, 6, 12, 21, 5, 3]
strings = ["lmn", "aaaaaaa", "w", "bb", "B", "cc"]
sorted_len_str = ["B", "w", "bb", "cc", "lmn", "aaaaaaa"]
part1 = [3, 5, 7, -11]
part2 = [0, 4, -10, -20]
merge_expected = [0, 3, 4, 5, 7, -10, -11, -20]

unittest_print.print_test(
    f"Sort of list {numbers}",
    sorted_numbers,
    hw8.bubble_sorted(numbers),
)
unittest_print.print_test(
    f"Sort of list {numbers} according to abs values",
    sorted_numbers_abs,
    hw8.bubble_sorted(numbers, abs),  # pyright: ignore[reportArgumentType]
)
unittest_print.print_test(
    f"Sort of list {numbers}: even ascending, then odd descending",
    sorted_even_odd,
    hw8.even_asc_odd_desc(numbers),
)
unittest_print.print_test(
    f"Sort of list {strings} by length, then by value",
    sorted_len_str,
    hw8.bubble_sorted(strings, lambda s: (len(str(s)), s)),
)
unittest_print.print_test(
    f"Merge {part1} and {part2} according to absolute values",
    merge_expected,
    hw8.merge(part1, part2, abs),  # pyright: ignore[reportArgumentType]
)

unittest_print.print_results()