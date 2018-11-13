# -*- coding:utf-8 _*_
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self,board):
        b = [[], [], [], [], [], [], [], [], []]
        c = [[], [], [], [], [], [], [], [], []]
        ans = []
        for i in range(9):
            for j in range(9):
                b[j].append(board[i][j])
                c[i // 3 * 3 + j // 3].append(board[i][j])
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    #找到可以填入的集合
                    for k in range(1,10):
                        if (str(k) not in board[i]) and (str(k) not in b[j]) and (str(k) not in c[i // 3 * 3 + j // 3]):
                            ans.append(str(k))
                    if ans==[]:
                        return False
                    for  k in ans:
                        board[i][j]=k
                        if  self.solve(board):
                            return True
                    board[i][j]='.'
                    return False
        return True
board=[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
o=Solution()
for i in o.solveSudoku(board):
    print(i)


