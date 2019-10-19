
class Trie:
    def __init__(self, letter = None):
        self.letter = letter
        self.vowels = None
        self.depth = None
        self.children = {}

    def add(self, word, w = 0, v = 0):
        if w == len(word):
            self.vowels = v
            self.depth = w
            return
        
        if word[w] in vowels:
            return self.add(word, w + 1, v + 1)
        else:
            if word[w] not in self.children:
                self.children[word[w]] = Trie(word[w])

            return self.children[word[w]].add(word, w + 1, v)

    def __repr__(self):
        return f"{self.letter}({self.vowels},{self.depth}): {self.children}"


vowels = "AEIOU"
root = Trie()

N = int(input())
for i in range(N):
    root.add(input())

print(root)

# Count the number of vowels per word
Q = input()



