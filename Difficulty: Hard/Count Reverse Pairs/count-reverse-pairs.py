class Solution:
    def countRevPairs(self, arr):
        # Code here
        import bisect
        cnt = 0
        def merge_sort(arr: list[int], lo: int, hi: int) -> list[int]:
            nonlocal cnt
            if lo == hi:
                return arr[lo:lo+1]
            mi = (lo+hi)//2
            a = merge_sort(arr, lo, mi)
            b = merge_sort(arr, mi+1, hi)
            r = []
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] < b[j]:
                    r.append(a[i])
                    i += 1
                else: #this branch can make sure b[j]*2 will be searched only once because j index will be incremented
                    searched = b[j]*2
                    k = bisect.bisect_right(a, searched)
                    cnt += len(a)-k
                    r.append(b[j])
                    j += 1
            while i < len(a):
                r.append(a[i])
                i += 1
            while j < len(b):
                r.append(b[j])
                j += 1
            return r 
        
        merge_sort(arr, 0, len(arr)-1)
        
        return cnt