class Solution:
    # pick a number between 0 and sum(weights) and
    #  map it to the index it corresponds to 
    # to find mapping, pick the index where rand([0, sum(wt)]) falls in prefix sum

    def __init__(self, w: List[int]):
        self.w = w
        self.total = sum(w)
        self.pre = []

        curSum = 0

        for wt in w:
            curSum += wt
            self.pre.append(curSum)
        

    def pickIndex(self) -> int:
        random_pick = self.total * random.random()
        # binary search for random_pick <= pre[i] 
        # this i is the res
        l, r = 0, len(self.w)
        res = None

        while l < r:
            mid = (l + r) // 2
            if self.pre[mid] <= random_pick:
                l = mid + 1
            else:
                r = mid
        
        return l
            

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()