class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        def isvalid(s):
            if s[0] == '0':
                return False
            if 0<int(s)<27:
                return True
            return False
        p = pp = 1
        if isvalid(s[:2]) is False:
            if isvalid(s[1]) is False:
                return 0
            
        
        if isvalid(s[:2]): 
            if isvalid(s[1]):
                p = 2
            else:
                p = 1
        
        c = 0
        for i in range(2,len(s)):
            #print (pp,p,c)
            curr = 0
            if isvalid(s[i]):
                curr = p
            if isvalid(s[i-1]+s[i]):
                curr+= pp
            if curr == 0:
                return 0
            pp,p = p,curr
        return p