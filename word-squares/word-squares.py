class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        '''
        b a l l
        a 
        l
        l
        '''
        trie = {}
        wlen = 0
        res = []
        for word in words:
            curr = trie
            wlen = len(word)
            for w in word:
                if w not in curr:
                    curr[w] = {}
                curr = curr[w]
            curr['#'] = word
        mat = [['' for _ in range(wlen)] for _ in range(wlen) ]
        def findInTrie(prefix):
            ret = []
            def helper(curr):
                if '#' in curr:
                    ret.append(curr['#'])
                else:
                    for k in curr.keys():
                        helper(curr[k])
            curr = trie
            for c in prefix:
                if c not in curr.keys():
                    return []
                curr = curr[c]
            helper(curr)
            return ret
        def helper(prefix, mat, r):

            possword  = findInTrie(prefix)
            for word in possword:
                for ri in range(r,wlen):
                    mat[r][ri] = word[ri]
                    mat[ri][r] = word[ri]
                if (r+1) == wlen:
                    res.append(["".join(row) for row in mat])
                else:
                    helper("".join(mat[r+1]), mat, r+1)
                for ri in range(r,wlen):
                    mat[r][ri] = ''
                    mat[ri][r] = ''
        helper("", mat, 0)
        return res