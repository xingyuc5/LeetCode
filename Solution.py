# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        
        return Solution.helper(self, root) != -1;

    def helper(self, root: TreeNode) -> int:
        """
        This function returns the heigth of a node if it is balanced, returns -1 otherwise
        """

        if root == None:
            return 0

        left = Solution.helper(self, root.left)
        if left == -1: 
            return -1
        right = Solution.helper(self, root.right)
        if right == -1:
            return -1
        
        return Math.max(left, right) + 1 if Math.abs(left - right) < 2 else -1
