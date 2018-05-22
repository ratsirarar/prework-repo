# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, root):
        stack = []
        b = root
        A = root
        while b:
            stack.append(b.val)
            b = b.next
            
        for i in range(len(stack)/2):
            elm = stack[-1]
            del(stack[-1])
            A.val = abs(A.val - elm)
            A = A.next
        return root

