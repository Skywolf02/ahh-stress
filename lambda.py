numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


evens = list(filter(lambda x: x % 2 == 0, numbers))


squares = list(map(lambda x: x ** 2, numbers))

print("Original numbers:", numbers)
print("Even numbers:", evens)
print("Squared numbers:", squares)