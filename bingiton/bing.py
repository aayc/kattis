class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
    
    def add(self, word):
        node = self
        for i in range(len(word)):
            if word[i] not in node.children:
                node.children[word[i]] = TrieNode()
            node.children[word[i]].count += 1
            node = node.children[word[i]]

    def find(self, word):
        node = self
        for i in range(len(word)):
            if word[i] not in node.children:
                return 0
            node = node.children[word[i]]
        return node.count

trie = TrieNode()
N = int(input())
for i in range(N):
    s = input()
    print(trie.find(s))
    trie.add(s)

