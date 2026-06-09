# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self, node):
        if not node: return 0

        left_height = self.check(node.left)
        right_height = self.check(node.right)

        if left_height == -1: return -1
        if right_height == -1: return -1
        
        if abs(left_height-right_height)>1: return -1

        return max(left_height, right_height) + 1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        return self.check(root) != -1


        