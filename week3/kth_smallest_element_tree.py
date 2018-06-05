# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        counter = []
        return self._inorder(A, counter)[B-1].val
    
    def _inorder(self, A, counter):
        if A.left:
            self._inorder(A.left, counter)
        counter.append(A)
        if A.right:
            self._inorder(A.right, counter)
        return counter
