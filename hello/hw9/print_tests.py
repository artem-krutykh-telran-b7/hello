import hw9


def print_test(description: str, expected: object, actual: object) -> None:
    result = "passed" if expected == actual else "failed"
    print(f"{description}: {result}; expected: {expected}; actual: {actual}")


items = [3, 5, 7, -11, 0, 4, -10, -20, 100, -80, -4, 8]
hw9.merge_in_place(items, start=0, len1=4, size=8, key=abs)
print_test(
    "Merge by absolute value",
    [0, 3, 4, 5, 7, -10, -11, -20, 100, -80, -4, 8],
    items,
)

items = [99, 3, 5, 7, 0, 4, 6, 100]
hw9.merge_in_place(items, start=1, len1=3, size=6)
print_test("Merge a subrange", [99, 0, 3, 4, 5, 6, 7, 100], items)

items = [1, 2, 3, 4]
hw9.merge_in_place(items, start=0, len1=2, size=4)
print_test("Already merged", [1, 2, 3, 4], items)

items = [3, 4, 1, 2]
hw9.merge_in_place(items, start=0, len1=2, size=4)
print_test("Reverse-ordered parts", [1, 2, 3, 4], items)

items = [2, 2, 1, 2]
hw9.merge_in_place(items, start=0, len1=2, size=4)
print_test("Duplicate values", [1, 2, 2, 2], items)

items = [-2, 2]
hw9.merge_in_place(items, start=0, len1=1, size=2, key=abs)
print_test("Equal keys keep their order", [-2, 2], items)

items = [3, 5, 7]
hw9.merge_in_place(items, start=0, len1=0, size=3)
print_test("Empty first part", [3, 5, 7], items)

items = [1, 2, 3]
hw9.merge_in_place(items, start=0, len1=3, size=3)
print_test("Empty second part", [1, 2, 3], items)
