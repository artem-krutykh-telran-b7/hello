import hw7


numbers = [10, 10, 10, 20, 20, 20, 30, 30, 40]

search_cases = [
    (10, 0),
    (20, 3),
    (40, 8),
    (5, -1),
    (15, -4),
    (50, -10),
]
for value, expected in search_cases:
    actual = hw7.binary_search(numbers, value)
    print(f"binary_search({value}), expected: {expected}, actual: {actual}")

insert_cases = [
    (7, [7, 10, 10, 10, 20, 20, 20, 30, 30, 40]),
    (19, [10, 10, 10, 19, 20, 20, 20, 30, 30, 40]),
    (20, [10, 10, 10, 20, 20, 20, 20, 30, 30, 40]),
    (45, [10, 10, 10, 20, 20, 20, 30, 30, 40, 45]),
]
for value, expected in insert_cases:
    actual = numbers.copy()
    hw7.insert_sorted(actual, value)
    print(f"insert_sorted({value}), expected: {expected}, actual: {actual}")
