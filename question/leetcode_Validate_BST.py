# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            value = node.val
            
            if value <= lower or value >= upper :
                return False
            
            
            if not helper(node.right, value, upper):
                return False
            if not helper(node.left, lower, value):
                return False
            
            return True
        
        return helper(root)


