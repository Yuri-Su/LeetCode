class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < 2 or numRows < 2:       return s
        
        trans = ["" for i in range(numRows)]
        row, mode, ans = 0, -1, ""
        for c in s:
            trans[row] = trans[row] + c
            if row == 0 or row == numRows - 1:  mode *= (-1)
            row += mode
        return "".join(trans)