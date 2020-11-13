# Your code here
def histogram():
    with open("robin.txt", "r") as file_output:
        data = file_output.read()

    words = data.split()
    cache = {}

    for word in words:
        word = word.lower().strip('":;,.-+=/\\|[]}{()*^&')
        if word not in cache:
            cache[word] = []

        cache[word].append("#")

    return cache

histo = histogram()

for word in histo:
    print("".join(histo[word]), word)