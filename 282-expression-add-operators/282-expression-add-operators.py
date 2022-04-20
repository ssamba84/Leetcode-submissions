class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        if int(num) == target and num[0] != '0':
            return [num]
        @lru_cache(None)
        def helper(i,expr):
            
            if i == len(num)-1:
                c = num[i]
                #print (i,expr, expr[-2] in '+*-' and expr[-1] != '0')
                if len(expr) >= 2:
                    if expr[-2] in '+*-':
                        if expr[-1] != '0' and eval(expr+c) == target:
                            res.append(expr+c)
                    elif eval(expr+c) == target:
                        res.append(expr+c)
                for op in '+*-':
                    exprop = expr+op+c
                    if eval(exprop) == target:
                        res.append(exprop)
                return
            for op in '+*-':
                helper(i+1, expr+op+num[i])
            #print (expr)
            if expr == '0':
                return
            if len(expr) >= 2:
                if expr[-2] in '+*-' and expr[-1] == '0':
                    return
            #print (expr+num[i], "X")
            helper(i+1, expr+num[i])
        helper(1,num[0])
        return res