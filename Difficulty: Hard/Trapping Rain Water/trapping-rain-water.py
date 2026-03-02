class Solution:
    def maxWater(self, arr):
        # code here
        n = len(arr)
        left, right = [0]*n, [0]*n
        m1, m2 = 0, 0
        for i in range(n):
            m1 = max(m1, arr[i])
            left[i] = m1
            m2 = max(m2, arr[n-1-i])
            right[n-1-i] = m2
        
        ans = 0
        for i in range(n):
            ans += min(left[i], right[i]) - arr[i]
        return ans