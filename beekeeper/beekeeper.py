vowels = set(["a", "e", "i", "o", "u", "y"])

def get_score(word):
    pairs = 0
    for i in range(1, len(word)):
        if word[i] == word[i - 1] and word[i - 1] in vowels:
            pairs +=1

    return pairs


while True:

    T = int(input())
    if T == 0:
        break

    max_word = ""
    max_score = -1
    for i in range(T):
        word = input()
        score = get_score(word)
        if score > max_score:
            max_score = score
            max_word = word
    print(max_word)
