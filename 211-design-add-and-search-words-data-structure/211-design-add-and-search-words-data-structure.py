class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['#'] = 1

    def search(self, word: str) -> bool:
        def helper(word, node):
            ret = False
            if len(word) == 0:
                return '#' in node
            c = word[0] 
            if  c == '.':
                for k in node.keys():
                    if k != '#':
                        ret |= helper(word[1:], node[k])
            else:
                if c not in node:
                    return False
                else:
                    return helper(word[1:], node[c])
            return ret
        return helper(word, self.trie)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)