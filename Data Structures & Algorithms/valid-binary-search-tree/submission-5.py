# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], lb: int, rb: int) -> bool:
            if not root:
                return True

            return lb < root.val < rb and dfs(root.left, lb, root.val) and dfs(root.right, root.val, rb)

        return dfs(root, float('-inf'), float('inf'))


        