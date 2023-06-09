class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        
        count = 0
        for r in range(len(grid) - 2):
            for c in range(len(grid[0]) - 2):
                if self.isvalid_square(grid, r, c):
                    count += 1
        return count
        
    def isvalid_square(self, grid, r, c):
        seen = set()
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                cell = grid[i][j]
                if not (1 <= cell <= 9) or cell in seen:
                    return False
                seen.add(cell)
                
        
        magic_sum = sum(grid[r][c:c+3])
        
        
        for i in range(r, r + 3):
            if sum(grid[i][c:c+3]) != magic_sum:
                return False
            
        
        for j in range(c, c + 3):
            if sum(grid[i][j] for i in range(r, r + 3)) != magic_sum:
                return False
            
        
        prim_sum, secon_sum = 0, 0
        for i in range(3):
            prim_sum += grid[r+i][c+i]
            secon_sum += grid[r+i][c+2-i]
        
        
        if prim_sum != magic_sum and secon_sum != magic_sum:
            return False
        
        return True
         
            
        