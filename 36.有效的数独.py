#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        """
        记录第i行数字curNum是否出现过
        """
        row = [[0] * 10 for _ in range(9)]
        col = [[0] * 10 for _ in range(9)]
        box = [[0] * 10 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                curNum = ord(board[i][j]) - ord('0')
                if row[i][curNum] != 0 or col[j][curNum] != 0 or box[j // 3 + (i // 3) * 3][curNum] != 0:
                    return False
                row[i][curNum], col[j][curNum],box[j // 3 + (i // 3) * 3][curNum] = 1, 1, 1
        return True
# @lc code=end

