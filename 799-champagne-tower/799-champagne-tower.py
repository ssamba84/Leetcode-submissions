class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0]*k for k in range(1,query_row+2)]
        tower[0][0] = poured
        for r in range(query_row):
            for c in range(r+1):
                amt = (tower[r][c]-1)/2
                if amt > 0:
                    tower[r+1][c] += amt
                    tower[r+1][c+1] += amt
        return min(tower[query_row][query_glass],1)