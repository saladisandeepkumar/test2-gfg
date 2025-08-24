class Solution:
    def minDaysBloom(self, arr, k, m):
        # Code here
        if k*m > len(arr):
            return -1
        
        def ok(day: int) -> bool:
            """given day, if it is possible to
               form m bouquets
            """
            nonlocal k, m
            i, cnt = 0, 0
            while i < len(arr):
                j = i
                while i < len(arr) and i-j+1 < k and arr[i] <= day:
                    i += 1
                if i == len(arr):
                    break
                if i-j+1 == k and arr[i] <= day:
                    cnt += 1
                i += 1
            return cnt >= m
                
                    
        # binary search the days that can form m bouquets.
        lo, hi = min(arr), max(arr)
        while lo < hi:
            mi = lo + (hi-lo)//2
            if ok(mi):  # we can decrrease mi
                hi = mi
            else:
                lo = mi+1
        return lo
        