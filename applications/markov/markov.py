import random

def markov(words):
    dictionary = {}

    words_split = words.split(" ")

    for i in range(len(words_split) - 1):
        word = words_split[i].lower().strip('":;,.!?-+=/\\|[]}{()*^&')
        next_word = words_split[i + 1].lower().strip('":;,.!?-+=/\\|[]}{()*^&')
        if word not in dictionary:
            dictionary[word] = {}

        if next_word not in dictionary[word]:
            dictionary[word][next_word] = 0

        dictionary[word][next_word] += 1

    for word in dictionary:
        next_words = dictionary[word]
        total = 0
        for word in next_words:
            count = next_words[word]
            total += count
        for word in next_words:
            next_words[word] /= total

    return dictionary
# Read in all the words in one go

with open("input.txt") as f:
    words = f.read()
    chain = markov(words)


    counter = 0
    while counter < 5:
        counter += 1
        sentence = ["the"]
        while len(sentence) < 8:
            chosen_var = random.random()
            word = sentence[-1]
            total = 0
            for next_word in chain[word]:
                total += chain[word][next_word]
                if total > chosen_var:
                    sentence.append(next_word)
                    break
        print(" ".join(sentence))

# TODO: analyze which words can follow other words
# Your code here



# TODO: construct 5 random sentences
# Your code here