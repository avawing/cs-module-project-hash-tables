def word_count(s):
    # Your code here
    cache = {}
    words_raw = s.split()
    words = []

    for x in words_raw:
        new_word = x.lower().strip('":;,.-+=/\|[]{}()*^&')
        words.append(new_word)

    unique_words = set(words)

    for word in unique_words:
        count = 0
        if word != "":
            for comparison in words:
                if word == comparison:
                    count += 1

            cache[word] = count

    return cache






if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))