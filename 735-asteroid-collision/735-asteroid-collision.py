class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        right = 0
        left = 1
        def collide(sn, n):
            if sn >= 0 and n < 0:
                return True
            return False
        i = 0
        while i < len(asteroids):
            n = asteroids[i]
            if not stk or collide((stk[-1]),(n)) is False:
                stk.append(n)
                i += 1
            else:
                while stk and collide((stk[-1]),(n)):
                    stktop = stk[-1]
                    if abs(stktop) < abs(n):
                        stk.pop()
                    elif abs(stktop) == abs(n):
                        stk.pop()
                        i += 1
                        break
                    else:
                        i += 1
                        break
        return stk