def digits_multiplication(number):

import functools
num1 = []
num = 123405
for i in str(num):
    num1.append(i)
num2 = list(map(int,num1))
cont1 = filter(lambda a: a != 0, num2)
print(functools.reduce(lambda x, y: x*y, cont1))
