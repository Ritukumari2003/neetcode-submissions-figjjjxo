# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, res, curr_max):
            if not node: return 0

            root_res = 0
            if node.val >= curr_max:
                root_res = 1
                curr_max = node.val
            
            left_res = dfs(node.left, res, curr_max)
            right_res = dfs(node.right, res, curr_max)

            return left_res + right_res + root_res
        
        return dfs(root, 0, float('-inf'))



        
        