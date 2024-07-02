class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        ans = 0
        row = {}
        col = {}
        for i in range(n):
            str_row = str(grid[i])
            row[str_row] = row.get(str_row, 0) + 1
            str_col = []
            for j in range(n):
                str_col.append(grid[j][i])
            col[str(str_col)] = col.get(str(str_col), 0) + 1

        for k, v in row.items():
            if col.get(k, 0) > 0 and v > 0:
                ans += v * col[k]
        return ans


