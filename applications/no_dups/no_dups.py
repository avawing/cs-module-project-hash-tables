def no_dups(s):
    # Your code here
    cache = {}

    words = s.split()
    solo_words = ""
    for word in words:
        if word not in cache:
            solo_words = solo_words + word + " "
            cache[word] = 1

    return solo_words.strip(" ")


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))