class TimeMap:

    def __init__(self):
        # ds = defaultdict([])
        # key - alice
        # value - [[timestamp1, val1], [timestamp1, val1] etc]
        # sorted according to timestamp val
        # set - ds[key].append([timestamp, value])
        # get - get the list ds[key]
        # search for the first value that is <= timestamp given using binary search
        self.ds = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ds[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # binary search on obtained list of values
        lst = self.ds[key]

        L, R = 0, len(lst) - 1
        res = ""
        while L <= R:
            M = (L + R)//2
            if lst[M][0] <= timestamp:
                res = lst[M][1]
                L = M + 1  
            else:
                R = M - 1
        
        return res

        
