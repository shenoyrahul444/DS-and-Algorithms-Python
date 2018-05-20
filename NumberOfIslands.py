class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.grid = grid
        # Edge Case
        if grid == None or grid == [] or grid == [[], [], []] or grid == [[]]:
            return 0

        self.row = len(grid)
        self.col = len(grid[0])

        cluster_count = 0
        visited = [[False for i in range(self.col)] for j in range(self.row)]

        for i in range(self.row):
            for j in range(self.col):

                if visited[i][j] == False and grid[i][j] == "1":
                    self.DFS(i, j, visited)
                    cluster_count += 1
        return cluster_count

    def DFS(self, row, col, visited):

        rows = [-1, 0, 1, 0]
        cols = [0, 1, 0, -1]

        visited[row][col] = True

        for k in range(len(rows)):
            if self.isSafe(row + rows[k], col + cols[k], visited):
                self.DFS(row + rows[k], col + cols[k], visited)

    def isSafe(self, row, col, visited):

        if 0 <= row < self.row and 0 <= col < self.col and visited[row][col] == False:
            if self.grid[row][col] == "1":
                return True
        else:
            return False

matrix = [["1","1","1","1","1"],["1","1","0","1","0"],["1","1","0","0","1"],["0","0","0","0","0"]]
sol = Solution()
print(sol.numIslands(matrix))