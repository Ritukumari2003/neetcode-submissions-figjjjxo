# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def validateBST(self, node, min_val=float('-inf'), max_val=float('inf')):
        if node is None:
            return True
        
        if not (min_val < node.val < max_val):
            return False
        
        return (self.validateBST(node.left, min_val, node.val) and
                self.validateBST(node.right, node.val, max_val))

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validateBST(root)