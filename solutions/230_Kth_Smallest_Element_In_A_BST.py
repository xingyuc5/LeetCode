# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.i = 0

        def preorder(root, k):
            if root:
                left = preorder(root.left, k)
                if left is not None:
                    return left
                self.i += 1
                if self.i == k:
                    return root.val
                right = preorder(root.right, k)
                if right is not None:
                    return right
            return
        return preorder(root, k)
