from functools import cache
@cache
def cnt(n):
    if n<=1:
        return 1
    ret=0
    for m in range(n):
        ret+=cnt(m)*cnt(n-1-m)
    return ret
cnt(6)

class Solution:
    def countBSTs(self, arr):
        lth=len(arr)
        tmp=sorted([*range(lth)],key=lambda x:arr[x])
        ret=[cnt(tmp.index(x))*cnt(lth-1-tmp.index(x)) for x in range(lth)]
        return ret