"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        ans=[]
        new=head
        while new:
            ans.append(new.data)
            new=new.next
        current=head
        while current:
            current.data=ans.pop()
            current=current.next
        return head
        
        