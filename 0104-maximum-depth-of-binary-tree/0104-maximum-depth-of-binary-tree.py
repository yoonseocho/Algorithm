# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if root is None:
            return max_depth
        q = deque()
        q.append((root, 1))

        while q:
            cur_node, cur_depth = q.popleft()
            max_depth = max(max_depth, cur_depth)

            if cur_node.left:
                q.append((cur_node.left, cur_depth + 1))
            if cur_node.right:
                q.append((cur_node.right, cur_depth + 1))
        return max_depth

