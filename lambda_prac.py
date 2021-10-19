# this file is to practice lambda
# lambda function is a small anonymous function
y = lambda x, z: x + z
print(y(1, 4))

# use lambda, map to do multiply
test_x = [1, 2, 3, 4, 5]
test_y = list(map(lambda r: r*5, test_x))
print(test_y)
assert test_x == [1, 2, 3, 4, 5]
assert test_y == [5, 10, 15, 20, 25], 'Results are incorrect'


# use dis module to disassemble python code
import dis
add = lambda x, y: x + y
# print(type(add)) # <class 'function'>
# print(dis.dis(add))
# print(add) # lambda

# the arguments style are the same way as the function parameter
sum_three = lambda x, y, z=3: x+y+z
print(sum_three(1, 2, 4))

# use arg parameter, and use * unpack all the parameter
sum_four = lambda *args: sum(args)
print(sum_four(1, 2, 3, 4))

