# -*- coding:utf-8 _*_



class Solution:
    ans=0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        table = []
        for i in range(n):
            table.append([False] * n)
        self.ans = 0
        self.solve(n, table, 0, self.ans)

        return self.ans

    def solve(self, n, table, k, ans):
        for i in range(n):
            table[k][i] = True
            if self.check(table, k, i, n):
                if k == n - 1:


                    self.ans+=1
                else:
                    self.solve(n, table, k + 1, ans)
            table[k][i] = False

    def check(self, table, k, l, n):
        for i in range(k):
            t = i + 1
            if table[i][l]:
                return False
            if t + l < n:
                if table[k - t][l + t]:
                    return False
            if l - t >= 0:
                if table[k - t][l - t]:
                    return False
        return True


o = Solution()
print(o.totalNQueens(4))
