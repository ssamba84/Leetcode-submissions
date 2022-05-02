class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        res = []
        ipaddr = [int(i) for i in ip.split('.')]
        def getips(n):
            res = 0
            i = 3
            ipi = ipaddr[i]
            while (ipi&1) ==0 and (n-(1<<res)) > 0:
                n -= 1<<res
                ipi = ipi>>1
                res += 1
                if (1<<res == 256):
                    i -= 1
                    ipi = ipaddr[i]
            return res
        def tocidr(nbits):
            res = ".".join([str(i) for i in ipaddr])
            res += '/'+str(32-nbits)
            return res
        def addtoipaddr(n):
            co =0
            i = 3#(3-(n//256))
            while i >=0 or co > 0:
                ipaddr[i] += n + co
                co = ipaddr[i]//256
                ipaddr[i] %= 256
                i -= 1
                n = 0
        while n > 0:
            ipn = getips(n)
            #print (1<<ipn)
            res.append(tocidr(ipn))
            
            n -= 1<<ipn
            #print (res, n)
            addtoipaddr(1<<ipn)
            #print (ipaddr)
        return res