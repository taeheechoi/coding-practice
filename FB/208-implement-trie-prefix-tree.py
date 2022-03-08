# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/1804957/Python-3-Easy-solution


class Trie:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = Trie()
            curr = curr.children[w]
        curr.is_end = True

    def search(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.is_end


    def startsWith(self, prefix):
        curr = self
        for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return True

    


























