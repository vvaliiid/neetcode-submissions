class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic_l = {}
        dic_c = {}
        dic_b = {}
        for i in range(9):
            dic_l[i] = set()
            dic_c[i] = set()        
            dic_b[i] = set()
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    if int(board[i][j]) in dic_l[i] or int(board[i][j]) in dic_c[j] or int(board[i][j]) in dic_b[((i//3)*3)+j//3]:
                        return False
                    else:
                        dic_l[i].add(int(board[i][j]))
                        dic_c[j].add(int(board[i][j]))
                        dic_b[((i//3)*3)+j//3].add(int(board[i][j]))
        return True