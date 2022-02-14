class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = [0]*26
        for k in tasks:
            k = ord(k)-ord('A')
            freq[k] += 1
        fmax = max(freq)
        fcount = freq.count(fmax)
        return max(len(tasks), (fmax-1)*(n+1)+fcount)