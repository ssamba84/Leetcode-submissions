class Solution:
    def expand(self, s: str) -> List[str]:
        res = []
        
        def getoptions(start):
            end = start
            while s[end]!='}':
                end += 1
            optionsubarray = s[start+1:end]
            return (optionsubarray.split(','), end+1)
        def helper(curr, i):
            if i == len(s):
                res.append(curr)
                return
            curri = i
            c = s[curri]
            if c == '{':
                options, curri = getoptions(curri)
                for option in options:
                    helper(curr+option,curri)
            else:
                helper(curr+c, i+1)
            
            
        helper("",0)
        res.sort()
        return res