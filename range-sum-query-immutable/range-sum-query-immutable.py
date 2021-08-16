class NumArray:

    def __init__(self, nums: List[int]):
        self.prefarr = nums.copy()
        acc = 0
        for i,n in enumerate(nums):
            acc += n
            self.prefarr[i] = acc

    def sumRange(self, left: int, right: int) -> int:
        ret = self.prefarr[right]
        if left > 0:
            ret -= self.prefarr[left-1]
        return ret


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)