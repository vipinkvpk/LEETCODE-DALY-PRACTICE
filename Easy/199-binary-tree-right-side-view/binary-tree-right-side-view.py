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
                current_node = queue.popleft()
                level.append(current_node.val)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                    # level.append(current_node.right.val)
            results.append(current_node.val)
        return results


        