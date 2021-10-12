class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        T = perf = l = 0
        for r, c in enumerate(calories):
            T += c
            if (r-l+1) == k:
                if  T < lower:
                    perf -= 1
                elif T > upper:
                    perf += 1
                T -= calories[l]
                l += 1
                
        return perf