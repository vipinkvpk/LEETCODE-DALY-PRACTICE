# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        queue= deque([root])
        results=[]
        while queue:
            level=[]
            level_size=len(queue)
            # current_value=[]
            for _ in range(level_size):
                current = queue.popleft()
                level.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                    level.append(current.right.val)
            results.append(current.val)
        return results


        