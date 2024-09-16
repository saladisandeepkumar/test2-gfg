# User function Template for Python3

class Solution:
    def maxLength(self, str):
        # code here
        st=[-1]
        max_count=0
        for i in range(len(str)):
            if str[i]=='(':
                st.append(i)
            else:
                st.pop()
            if not st:
                st.append(i)
            else:
                max_count=max(max_count,i-st[-1])
        return max_count


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))

# } Driver Code Ends