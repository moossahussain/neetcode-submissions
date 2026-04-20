class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0

        if not grid:
            return
        
        def dfs(r, c):
            # base cases
            if r < 0 or r >= len(grid): return

            if c < 0 or c >= len(grid[0]): return

            if grid[r][c] == '0': return

            # marking processed to avoid revisiting
            grid[r][c] = '0'

            # recursion
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count +=1
                    dfs(r,c)


        return count

