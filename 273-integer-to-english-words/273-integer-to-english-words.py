class Solution:
    def numberToWords(self, num: int) -> str:
        ht1 = {1:'One', 2:'Two', 3:'Three',4:'Four',5:'Five', 6:'Six',7:'Seven',8:'Eight',9:'Nine'}
        ht2 = {2:'Twenty', 3:'Thirty', 4: 'Forty', 5:'Fifty', 6: 'Sixty', 7: 'Seventy', 8:'Eighty', 9: 'Ninety'}
        ht3 = {10:'Ten', 11: 'Eleven', 12: 'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
        res = []
        if num == 0:
            return 'Zero'
        #print (num)
        if num < 1000:
            h = num//100
            if h > 0:
                res += [ht1.get(h,''), 'Hundred']
            num %= 100
            if 9<num<20:
                res += [ht3.get(num, '')]
            elif num > 0:
                t = num//10
                num %= 10
                if t > 0:
                    res += [ht2.get(t,'')]
                if num > 0:
                    res += [ht1.get(num,'')]
        else:
            if 1000<=num < 1000000:
                res += [self.numberToWords(num//1000), 'Thousand']
                num %= 1000

            elif 1000000<=num < 1000000000:
                res += [self.numberToWords(num//1000000), 'Million']
                num %= 1000000
            else:
                res += [self.numberToWords(num//1000000000), 'Billion']
                num %= 1000000000
            if num > 0:
                res += [self.numberToWords(num)]
        return " ".join(res)