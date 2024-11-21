from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        n = len(prices)
        maxi = 0
        l,r = 0,0
        while r<n-1:
            if prices[r]<=prices[r+1]:
                profit = prices[r+1]-prices[l]
                maxi+=profit
            r+=1
            l+=1
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)

# } Driver Code Ends