class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x,y in list(self.ptsCount.keys()):
            if (abs(px - x) != abs(py - y)) or px == x or py == y:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)] * self.ptsCount[(x,y)]
        
        return res
