# The map() function applies a function to every member of an iterable and returns the result.
# example 1:
def square(x):
    return x ** 2


list_a = [1, 2, 3, 4, 5]
# map return an iterable object, how to print them out? use list(return_object)
square_results = map(square, list_a)
print(list(square_results))

# example 2: use built-in functions instead of self-designed one
names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
lengths = map(len, names)
print(list(lengths))

# example 3: use built-in functions like max
arrays = [[1, 2, 3], [9, 2, 1]]
max_val = map(max, arrays)
print(list(max_val))

# we can use map and lambda together
squares_result = map(lambda x: x**2, range(10))
print(list(squares_result))


# list comprehensions, first-loop is out-loop and second-loop is inner-loop
possible_choices = [[drink, food] for drink in ['water', 'tea', 'juice'] for food in ['ham', 'eggs', 'spam']]
print(possible_choices)
