# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            lst = []
            for _ in range(len(queue)):
                ele = queue.popleft()
                if ele:
                    lst.append(ele.val)
                    queue.append(ele.left)
                    queue.append(ele.right)
            if lst:
                res.append(lst)
        return res


        