class Solution:
    # pick a number between 0 and sum(weights) and
    #  map it to the index it corresponds to 
    # to find mapping, pick the index where rand([0, sum(wt)]) falls in prefix sum

    def __init__(self, w: List[int]):
        self.w = w
        self.total = sum(w)
        

    def pickIndex(self) -> int:
        random_pick = self.total * random.random()
        curSum = 0

        for i in range(len(self.w)):
            curSum += self.w[i]
            if curSum > random_pick:
                return i
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()