class Solution:
    def isHappy(self, n: int) -> bool:
        def sos(n):
            res = 0
            while n > 0:
                d = n%10
                res += d*d
                n //= 10
            return res
        slow = fast = n
        while slow != 1:
            
            slow = sos(slow)
            fast = sos(sos(fast))
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False
        return True
                