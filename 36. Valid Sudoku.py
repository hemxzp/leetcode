# -*- coding:utf-8 _*_
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        b=[[],[],[],[],[],[],[],[],[]]
        c=[[],[],[],[],[],[],[],[],[]]
        for i in range(9):
            for j in range(9):
                b[j].append(board[i][j])
                c[i//3*3+j//3].append(board[i][j])
        for i in board:
            if not self.check(i):
                return False
        for i in b:
            if not self.check(i):
                return False
        for i in c:
            if not self.check(i):
                return False
        return True
    def check(self,l):
        times=[]
        for i in l:
            if i!='.':
                if i in times:
                    return False
                else:
                    times.append(i)
        return True
tem=[
  ["8","3",".",".","7",".",".",".","."],
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
print(o.isValidSudoku(tem))