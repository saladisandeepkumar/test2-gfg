class Solution:
    def checkSorted(self, arr):
        n=2
        i=0
        end=len(arr)
        while i<end:
            if arr[i]!=(i+1):
                if n<1:
                    return False
                n-=1
                # require a temp variable to swap in this case as 2 elements have interdependent logics
                temp=arr[arr[i]-1]
                arr[arr[i]-1]=arr[i]
                arr[i]=temp
            else:
                i+=1
        if n==1:
            return False
        return True


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends