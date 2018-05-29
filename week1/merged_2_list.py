# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    # [ 7 -> 12 -> 46 -> 66
    # [ 12 -> 22 -> 27 -> 29 
    def mergeTwoLists(self, A, B):
        x = A
        y = B
        merged_root = None
        
        if x.val <= y.val:
            merged_root = x
            x = x.next
        else: 
            merged_root = y
            y = y.next
        merged_root.next = None
        
        pointer_merge = merged_root
        
        while x and y:
            if x.val <= y.val:
                tmp = x.next
                pointer_merge.next = x
                pointer_merge = pointer_merge.next
                pointer_merge.next = None
                x = tmp
            else:
                tmp = y.next
                pointer_merge.next = y
                pointer_merge = pointer_merge.next
                pointer_merge.next = None
                y = tmp
        if x:
            pointer_merge.next = x
        elif y:
            pointer_merge.next = y
        return merged_root
                
        
