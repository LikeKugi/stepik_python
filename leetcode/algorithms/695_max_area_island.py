class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        checked = set()
        current_max = 0
        total_max = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                # print(checked)
                if cell == 1 and (i, j) not in checked:
                    current_max = self.find_area(checked, grid, i, j, current_max)

                    if current_max > total_max:
                        total_max = current_max
                    current_max = 0
        return total_max

    def find_area(self, checked, grid, i, j, current_max):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
            if grid[i][j] == 1 and (i, j) not in checked:
                checked.add((i, j))
                current_max += 1
                current_max = self.find_area(checked, grid, i - 1, j, current_max)
                current_max = self.find_area(checked, grid, i, j - 1, current_max)
                current_max = self.find_area(checked, grid, i + 1, j, current_max)
                current_max = self.find_area(checked, grid, i, j + 1, current_max)
        return current_max