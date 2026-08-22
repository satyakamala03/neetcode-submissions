class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = []

        for s in strs:
            zeroes = s.count("0")
            ones = s.count("1")
            counts.append((zeroes, ones))

        state = {}
        
        def memo(i, rem_m, rem_n):
            # no strings left
            if i == len(strs):
                return 0
            
            if (i,rem_m,rem_n) in state:
                return state[(i,rem_m,rem_n)]
            
            zeroes, ones = counts[i]
            # skip
            best = memo(i+1, rem_m, rem_n)
            if zeroes <= rem_m and ones <= rem_n:
                best = max(best, 1 + memo(i+1, rem_m - zeroes, rem_n - ones))
            
            state[(i,rem_m,rem_n)] = best
            return best
        
        return memo(0,m,n)