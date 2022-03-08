# https://leetcode.com/problems/design-add-and-search-words-data-structure/discuss/1725327/JavaC%2B%2BPython-A-very-well-detailed-EXPLANATION!


class WordDictionary:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
    
    def addWord(self, word):
        curr = self
       
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordDictionary()
            curr = curr.children[c]
        curr.isEndOfWord = True

    
    def search(self, word):
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.children:
                    if ch != None and self.search(word[i+1:]):
                        return True
                return False

            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr != None and curr.isEndOfWord


wd = WordDictionary()
wd.addWord('bad')
