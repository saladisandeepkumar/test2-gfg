class Solution:
    def smallestWindow(self, s, p):
        # code here
        from collections import Counter
        
        need = Counter(p)
        need_count = len(need)  
        have = 0
        window = {}
        
        res, res_len = [-1, -1], float("inf")
        left = 0
        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_count:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
        