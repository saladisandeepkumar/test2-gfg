class Solution:
    def minTime(self, root, target):
        def dfs(cur=root):
            nonlocal target
            if not cur:
                return -float('inf'),0,-float('inf')
            l=dfs(cur.left)
            r=dfs(cur.right)
            if cur.data==target:
                return max(l[1],r[1]),max(l[1],r[1])+1,0
            a=max(l[0],r[0],l[2]+r[1]+1,r[2]+l[1]+1)
            b=max(l[1],r[1])+1
            c=max(l[2],r[2])+1
            return a,b,c
            '''
            a: minimum time required.
            - from target node in 1 of subtree to the deepest leave of the alternate subtree, or
            - from target node via a specific subnode to the deepest leave seen of that said specific subnode
            b: depth of deepest leave from current node
            c: depth of target from current node
            '''
        return dfs()[0]