#User function Template for python3
from collections import deque 
class Solution:
    def minSum(self, arr):
        # code here
        n=len(arr)
        arr.sort(reverse=True)
        ans=deque()
        carry=0
        i=0
        while i<n and arr[i]!=0:
            val=arr[i]+carry
            if (i+1)<n:
                val+=arr[i+1]
            carry=val//10
            val=val%10
            ans.appendleft(str(val))
            i+=2
        if carry:
            ans.appendleft("1")
        return "".join(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSum(arr)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends