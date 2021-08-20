class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R = len(board)
        C = len(board[0])
        mask = 0
        for r in range(R):
            mask = 0
            for c in range(C):
                n = board[r][c]
                if n == '.':
                    continue
                n = int(n)
                if mask&(1<<n):
                    return False
                mask |= (1<<n)
        for c in range(C):
            mask = 0
            for r in range(R):
                n = board[r][c]
                if n == '.':
                    continue
                n = int(n)
                if mask&(1<<n):
                    return False
                mask |= (1<<n)
        for i in range(0,9,3):
            for j in range(0,9,3):
                rstart = i
                cstart = j
                mask = 0
                for r in range(rstart,rstart+3):
                    for c in range(cstart, cstart+3):
                        n = board[r][c]
                        if n == '.':
                            continue
                        n = int(n)
                        if mask&(1<<n):
                            return False
                        mask |= (1<<n)
        return True