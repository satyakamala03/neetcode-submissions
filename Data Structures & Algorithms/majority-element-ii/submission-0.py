class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
            if len(counts) > 2:
                for k in counts.keys():
                    counts[k] -= 1
                new_cnt = {}
                for k,v in counts.items():
                    if counts[k] > 0:
                        new_cnt[k] = v
                counts = new_cnt
        
        res = []
        for k in counts.keys():
            cnt = 0
            for n in nums:
                if k == n:
                    cnt += 1
            if cnt > len(nums) // 3:
                res.append(k)
        
        return res



            