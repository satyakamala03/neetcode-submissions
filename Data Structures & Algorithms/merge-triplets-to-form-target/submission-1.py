class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if target in triplets:
            return True
        
        valid = []
        
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            valid.append(t)
        
        a = b = c = False

        for v in valid:
            if v[0] == target[0]:
                a = True
            if v[1] == target[1]:
                b = True
            if v[2] == target[2]:
                c = True
        
        return (a and b and c)
