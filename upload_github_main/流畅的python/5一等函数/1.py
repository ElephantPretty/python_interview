def factorial(n):
    """returns n"""
    return 1 if n < 2 else n * factorial(n - 1)

# print(factorial(42))
# print(factorial.__doc__)
# print(type(factorial))

# fact = factorial
# print(fact)
# print(fact(5))
# print(map(factorial, range(11)))
# print(list(map(fact, range(11))))

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))