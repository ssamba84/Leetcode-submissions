class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R = len(board)
        res = set()
        if R == 0:
            return res
        C = len(board[0])
        neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
        trie = {}
        for word in words:
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['#'] = 1
        def dfs(r,c, node, cword, cpath):
            
            if r < 0 or r >= R or c<0 or c>=C :
                return
            if '#' in node:
                res.add(cword)
            for i,j in neighbors:
                ri = r+i
                cj = c+j
                
                if 0<=ri<R and 0<=cj<C and ((ri,cj) not in cpath):
                    cc = board[ri][cj]
                    if cc in node:
                        cpath[(ri,cj)] = 1
                        dfs(ri,cj, node[cc], cword+cc, cpath)
                        del ht[(ri,cj)]
        
        for r in range(R):
            for c in range(C):
                cc = board[r][c]
                if cc in trie:
                    ht = {}
                    ht[(r,c)] = 1
                    dfs(r,c,trie[cc], cc, ht)
        return res
        
                    