# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
most_freq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
             'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
with open("ciphertext.txt", "r") as file_output:
    data = file_output.read()
    letters = [letter for letter in data]

    freq = {}
    for letter in letters:
        if letter not in most_freq:
            continue
        if letter not in freq:
            freq[letter] = 0
        freq[letter] += 1

    ordered_freq = [letter for letter in freq]

    def sorter(letter):
        return freq[letter]

    ordered_freq.sort(key=sorter, reverse=True)
    story = ""
    for letter in letters:
        if letter not in ordered_freq:
            story = story + letter
            continue
        index = ordered_freq.index(letter)
        new_letter = most_freq[index]
        story = story + new_letter

    print(story)


# Your code here

