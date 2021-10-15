class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(n):
            res = 0
            while n:
                res += (n%10)**2
                n //= 10
            return res
        slow = fast = n
        while fast != 1:
            slow = happy(slow)
            fast = happy(fast)
            if fast == 1:
                break
            fast = happy(fast)
            if slow == fast:
                return False
        return True