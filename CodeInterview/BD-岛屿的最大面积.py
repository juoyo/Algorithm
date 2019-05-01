class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxS = 0
        for i in range(0, len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    num = self.deepSearch(grid, i, j)
                    maxS = max(num, maxS)
        return maxS
    def deepSearch(self, grid, i, j):
        if(i>=0 and i<len(grid) and j>=0 and j<len(grid[0]) and grid[i][j]==1):
            grid[i][j]=0
            left = self.deepSearch(grid, i-1, j)
            right = self.deepSearch(grid, i+1, j)
            down = self.deepSearch(grid, i, j-1)
            up = self.deepSearch(grid, i, j+1)
            num = 1+left+right+down+up
            return num
        else:
            return 0

s = Solution()
print(s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))









