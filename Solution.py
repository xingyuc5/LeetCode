# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        root = Solution.recursive_insert(0, len(nums)-1, nums)
        return root

    def recursive_insert(self, low: int, high: int, nums: List[int]) -> TreeNode:
        if low > high:
            return None

        mid = (low + high) // 2
        node = TreeNode(nums[mid])
        node.left = Solution.recursive_insert(low, mid-1)
        node.right = Solution.recursive_insert(mid+1, high)
        return node
