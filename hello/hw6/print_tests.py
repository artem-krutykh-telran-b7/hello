import random

import hw6


print(
    "max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100]), "
    f"expected: 100, actual: {hw6.max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100])}"
)
print(
    "max_with_negative_duplicate([-100, 100, 20, 10, -10, 110, 1, 5, -30, -20, -110]), "
    f"expected: 110, actual: {hw6.max_with_negative_duplicate([-100, 100, 20, 10, -10, 110, 1, 5, -30, -20, -110])}"
)
print(
    "max_with_negative_duplicate([10, 20, -15, -11, 20]), "
    f"expected: -1, actual: {hw6.max_with_negative_duplicate([10, 20, -15, -11, 20])}"
)
print(
    "sumOfTwoExists([100, -10, 12, 12, -100], 24), "
    f"expected: True, actual: {hw6.sumOfTwoExists([100, -10, 12, 12, -100], 24)}"
)
print(
    "sumOfTwoExists([100, -10, 12, 12, -100], 0), "
    f"expected: True, actual: {hw6.sumOfTwoExists([100, -10, 12, 12, -100], 0)}"
)
print(
    "sumOfTwoExists([100, -10, 12, 12, -100], 25), "
    f"expected: False, actual: {hw6.sumOfTwoExists([100, -10, 12, 12, -100], 25)}"
)

numbers = [random.randint(1, 1000) for _ in range(1000)]
hw6.bubble_sort(numbers)
print(f"bubble_sort produces sorted numbers: {numbers == sorted(numbers)}")

numbers = [1, 8, 0, -1, 1, 10, 1_000_000, 8]
print(
    f"remove_duplicates({numbers}), "
    f"expected: [1, 8, 0, -1, 10, 1000000], actual: {hw6.remove_duplicates(numbers)}"
)
