class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        n=arr.sort()
        i=0
        j=len(arr)-1
        res=[]
        while i<=j:
            res.append(arr[j])
            if arr[i]!=arr[j]:
                res.append(arr[i])
            i+=1
            j-=1
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        # print("~")
        t -= 1

# } Driver Code Ends