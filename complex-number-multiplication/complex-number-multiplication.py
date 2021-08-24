class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1,i1 = num1.split("+")[0],num1.split("+")[1][:-1]
        r2,i2 = num2.split("+")[0],num2.split("+")[1][:-1]
        r1 = int(r1)
        i1 = int(i1)
        r2 = int(r2)
        i2 = int(i2)
        rr = r1*r2-i2*i1
        ri = (i2*r1)+(r2*i1)
        
        return str(rr)+"+"+str(ri)+'i'