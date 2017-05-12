def num(i):
    print(''.join("Fizz"*(i%3==0)+"Buzz"*(i%5==0)))

num(7)


def long_num(i):
    if i % 3 == 0 and i % 5 == 0:
        return 'Fizz Buzz'
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'

long_num(15)
