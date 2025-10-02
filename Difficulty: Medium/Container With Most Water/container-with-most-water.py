class Solution:
    def maxWater(self, arr):
        # code here
        n = len(arr)
        left, right = 0, n - 1
        res = 0

        while left < right:
            width = right - left
            height = min(arr[left], arr[right])
            res = max(res, width * height)

            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1

        return res
        