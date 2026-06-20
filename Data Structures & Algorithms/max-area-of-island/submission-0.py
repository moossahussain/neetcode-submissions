class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):
            if r < 0 or r >= len(grid): return 0
            if c < 0 or c >= len(grid[0]):  return 0
            if grid[r][c] == 0: return 0

            grid[r][c] = 0
            area=1


            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)

            return area



        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] == 1:
                    area = dfs(r, c)
                    count = max(count, area)

        return count