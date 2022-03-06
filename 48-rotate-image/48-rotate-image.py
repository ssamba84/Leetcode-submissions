class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        00 01 02
        10 11 12   
        20 21 22
        
        20 10 00
        21 11 01
        22 12 02
        """
        
        n = len(matrix)
        for k in range(n//2):
            for i in range(k,n-k-1):
                tl = matrix[k][i]
                tr = matrix[i][n-1-k]
                bl = matrix[n-1-k][n-1-i]
                br = matrix[n-1-i][k]
                #print(tl,tr,bl,br)
                matrix[k][i],matrix[i][n-1-k],matrix[n-1-k][n-1-i],matrix[n-1-i][k] = br,tl,tr,bl
                
        