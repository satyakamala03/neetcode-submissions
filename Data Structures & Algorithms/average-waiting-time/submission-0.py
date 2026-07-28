class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        nxt_st_time = 0
        cum_wait_time = 0

        for arr, prep in customers:
            nxt_st_time = max(nxt_st_time, arr)
            print(f"next st time: {nxt_st_time}")

            wait_time = nxt_st_time + prep - arr
            print(f"wait time: {wait_time}")
            cum_wait_time += wait_time
            nxt_st_time += prep
        
        res = cum_wait_time / len(customers)

        return res