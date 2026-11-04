import hw5

numbers = [2, 4, 6]
print(f"minMaxAverage({numbers}), expected: (2, 6, 4.0), actual: {hw5.minMaxAverage(numbers)}")
numbers = [100, 20, 30, 40, 50]
before = numbers.copy()
hw5.moveMaxToEnd(numbers)
print(f"moveMaxToEnd({before}), expected: [20, 30, 40, 50, 100], actual: {numbers}")

numbers = [1, 2, 3]
before = numbers.copy()
hw5.moveMaxToEnd(numbers)
print(f"moveMaxToEnd({before}), expected: [1, 2, 3], actual: {numbers}")

numbers = [5, 1, 5, 2]
before = numbers.copy()
hw5.moveMaxToEnd(numbers)
print(f"moveMaxToEnd({before}), expected: [1, 5, 2, 5], actual: {numbers}")

numbers = [7]
before = numbers.copy()
hw5.moveMaxToEnd(numbers)
print(f"moveMaxToEnd({before}), expected: [7], actual: {numbers}")