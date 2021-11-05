class Solution:
    def arrangeCoins(self, n: int) -> int:
        '''
        ax2 + bx + c
        
        ( (b2 - 4ac)**.5 -b)-n / 2a
        x2  + x -2n = 0 
        
        '''
        return int((((1+8*n)**.5) - 1)//2)