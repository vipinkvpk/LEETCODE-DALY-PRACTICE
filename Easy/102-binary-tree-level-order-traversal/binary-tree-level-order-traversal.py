# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:       
        # if root is None:
        #     return []
        # current_node=root
        # queue=[]
        # results=[]
        # queue.append(current_node)
        # while queue:
        #     level_size=len(queue)
        #     level=[]
        #     for _ in range(level_size):
        #         current_node= queue.pop(0)
        #         level.append(current_node.val)
        #         if current_node.left:
        #             queue.append(current_node.left) 
        #         if current_node.right:
        #             queue.append(current_node.right) 
        #     results.append(level)
        # return results
        if not root:
            return []  # If the tree is empty, return an empty list

        queue = deque([root])  # Start with the root node in the queue
        result = []            # This will store the final level order traversal

        while queue:
            level = []  # List to store values of the current level
            level_size = len(queue)  # Number of nodes at the current level

            for _ in range(level_size):
                current_node = queue.popleft()  # Get the front node from the queue
                level.append(current_node.val)  # Add its value to the current level list

                # Add left and right children to the queue if they exist
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            result.append(level)  # Add the completed level to the result

        return result

        