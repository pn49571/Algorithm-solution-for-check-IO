def most_number(*args):
    lst = []
    if len(args) != 0:
        for x in args:
            lst.append(x)
        return (max(lst) - min(lst))
    else:
        return 0

most_number()
