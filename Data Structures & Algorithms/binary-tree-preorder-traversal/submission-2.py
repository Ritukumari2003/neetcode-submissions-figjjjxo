# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return res

        stk = []
        
        stk.append(root)
        while stk:
            node = stk[-1]
            stk.pop()
            res.append(node.val)
            if node.right: stk.append(node.right)
            if node.left: stk.append(node.left)
        return res

            


              