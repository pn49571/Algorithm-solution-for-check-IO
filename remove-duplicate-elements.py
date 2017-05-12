def checkio(data):
    return [x for x in data if data.count(x) > 1]
if __name__ == "__main__":
    print(checkio([1, 2, 3, 1, 3]))

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
