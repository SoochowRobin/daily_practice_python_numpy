# decorator is a milestone for Python developer

# level 0: Understand the basic concepts and usages: what is a decorator
def add_author(func):
    print('Robin Chen')
    return func


# in the context of functional programming, our decorators which contain nested functions are named closures
def add_things(func):
    def wrapper():
        title = func()
        # new title will add more ! through inner function
        new_title = title + "!!!!!!"
        return new_title
    return wrapper()


# call decorator
@add_author
def get_title():
    return '7 levels of Using Decorators in Python'


print(get_title())

# get_title2 will use inner function
@add_things
def get_title2():
    return '7 levels of Using Decorators in Python'

print(get_title2)