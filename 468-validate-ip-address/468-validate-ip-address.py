class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        IPv4 = "IPv4"
        IPv6 = "IPv6"
        Neither = "Neither"
        def isvalidipv4quartet(ipv4q):
            if len(ipv4q) > 1 and ipv4q[0] == '0' or ipv4q.isdigit() is False:
                return False
            if 0<=int(ipv4q)<=255:
                return True
            return False
        def isvalidipv4(ipv4):
            ipv4split = ipv4.split('.')
            if len(ipv4split) != 4:
                return False
            
            return all(isvalidipv4quartet(ip) for ip in ipv4split)
        def v6helper(ipv6):
            if len(ipv6)>4 or len(ipv6) == 0:
                return False
            
            if ipv6.isdigit():
                return True
            chars = "".join([c for c in ipv6 if c.isalpha()])
            #print (ipv6,(chars.isupper() is False) , (chars.islower() is False) )
            #if (chars.isupper() is False) and (chars.islower() is False):
            #    return False
            for c in 'ghijlkmnopqrstuvwxyz':
                if c in chars.lower():
                    return False
            return True
            
        def isvalidipv6(ipv6):
            ipv6split = ipv6.split(':')
            if len(ipv6split) != 8:
                return False
            return all(v6helper(ip) for ip in ipv6split)
        if isvalidipv4(queryIP):
            return IPv4
        if isvalidipv6(queryIP):
            return IPv6
        return Neither