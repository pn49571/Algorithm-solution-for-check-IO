def three_words(alphabet):
    count = 0
    for j in alphabet.split():
        if j.isalpha():
            count += 1
        else:
            count = 0
        if (count  == 3):
            return True
            break
    return False

three_words("Hello im 123")
