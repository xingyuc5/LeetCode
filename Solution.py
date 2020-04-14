# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return None

        nodes = Solution.helper(self, root, [])
        return nodes

    def helper(self, root: TreeNode, nodes: List):
        if root is None:
            return

        Solution.helper(self, root.left, nodes)
        nodes.append(root.val)
        Solution.helper(self, root.right, nodes)
        return nodes
