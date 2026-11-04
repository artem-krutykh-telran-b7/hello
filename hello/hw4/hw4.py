def intersection(l1: list[int], l2: list[int]) -> list[int]:
    return [n for n in l1 if n in l2]

def difference(l1: list[int], l2: list[int]) -> list[int]:
    return [n for n in l1 if n not in l2]

def union(l1: list[int], l2: list[int]) -> list[int]:
    result = l1.copy()
    for n in l2:
        if n not in result:
            result.append(n)
    return result

def symmetric_difference(l1: list[int], l2: list[int]) -> list[int]:
    result = difference(l1, l2)
    for n in l2:
        if n not in l1:
            result.append(n)
    return result