# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        return Solution.helper(self, 1, n)

    def helper(self, low: int, high: int) -> List[TreeNode]:
        trees = []

        if low > high:
            trees.append(None)
            return trees

        for i in range(low, high+1):

            leftSubTree = Solution.helper(self, low, i-1)
            rightSubtree = Solution.helper(self, i+1, high)

            for j in range(len(leftSubTree)):
                left = leftSubTree[j]

                for k in range(len(rightSubtree)):
                    right = rightSubtree[k]
                    node = TreeNode(i)
                    node.left = left
                    node.right = right
                    trees.append(node)
        return trees
