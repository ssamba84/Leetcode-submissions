class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ht = defaultdict(int)
        for cpd in cpdomains:
            c, dom = cpd.split(' ')
            c = int(c)
            prev = []
            for d in dom.split('.')[::-1]:
                prev = [d]+prev
                #print (".".join(prev))
                ht[".".join(prev)] += c
        return ["{} {}".format(d,c) for c,d in ht.items()]