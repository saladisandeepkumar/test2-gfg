#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        n=len(arr)
        res=0
        max_val=arr[0]
        for i in range(0,n):
            res +=arr[i]
            max_val=max(res,max_val)
            
            if res<0:
                res=0
        return max_val


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends