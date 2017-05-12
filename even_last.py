def even_last(number):
    if(len(number) != 0):
        return number[-1] * sum([ j for i,j in enumerate(number) if (i%2 == 0)])
    else:
        return 0


even_last([])
