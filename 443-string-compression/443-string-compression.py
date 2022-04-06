class Solution:
    def compress(self, chars: List[str]) -> int:
        currsum = 1
        wi = 0
        '''
        ["a","a","b","b","c","c","c"]
                  c
         cs 1
         p a
        '''
        prev = chars[0]
        for i,c in enumerate(chars):
            if i == 0:
                continue
            if c == prev:
                currsum += 1
            else:
                if currsum == 1:
                    chars[wi] = prev
                    wi += 1
                else:
                    num = str(currsum)
                    chars[wi] = prev
                    wi += 1
                    for n in num:
                        chars[wi] = n
                        wi += 1
                    currsum = 1
            prev = c
        if currsum == 1:
            chars[wi] = prev
            wi += 1
        else:
            num = str(currsum)
            chars[wi] = prev
            wi += 1
            for n in num:
                chars[wi] = n
                wi += 1
        return wi