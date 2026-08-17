class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og_color = image[sr][sc]

        if og_color == color:
            return image

        ROWS, COLS = len(image), len(image[0])
        visit = set()
        delta = [[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r, c):
            if min(r,c) < 0 or r == ROWS or c == COLS or image[r][c] != og_color or (r,c) in visit:
                return
            
            visit.add((r,c))
            image[r][c] = color

            for dr, dc in delta:
                dfs(r + dr, c + dc)
        
        dfs(sr, sc)

        return image