# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        queue = deque()
        max_val =  float('-inf')
        queue.append((root,max_val))
        res = 0

        while queue:
            ele = queue.popleft()
            node = ele[0]
            max_val = ele[1]
            if ele[0].val >= max_val:
                res += 1
                max_val = ele[0].val
            if ele[0].left:
                queue.append((ele[0].left, max_val))
            if ele[0].right:
                queue.append((ele[0].right, max_val))
        
        return res
            
