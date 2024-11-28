#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Code here
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return 0
            
        sign = 1
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign *= -1
            i += 1
        if i == len(s): 
            return 0
            
        while i < len(s) and s[i] == '0':
            i += 1
        if i == len(s):
            return 0
            
        j = i
        while j < len(s) and s[j].isdigit(): 
            j += 1
        
        s = s[i:j]
        if sign == 1 and (len(s)> 10 or (len(s) == 10 and s > str(2**31-1))):
            return 2**31-1
        if sign == -1 and (len(s) > 10 or (len(s) == 10 and s > str(2**31))):
            return -2**31
        ans = 0
        for i in range(len(s)):
            ans = ans*10 + (ord(s[i])-ord('0'))
        return sign * ans


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends