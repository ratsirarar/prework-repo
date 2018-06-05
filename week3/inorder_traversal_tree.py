# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        res = []
        self._inorder(A, res)
        return res
    
    def _inorder(self, A, res):
        if A.left:
            self.inorderTraversal(A.left)
        res.append(A.val)
        if A.right:
            self.inorderTraversal(A.right)

