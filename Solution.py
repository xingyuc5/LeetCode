# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        # Empty Queue to be returned as result
        queue = []

        # Current layer has only root node
        cur = [root]

        # While current layer is not Empty
        while cur:

            # Initialize empty lists
            cur_layer_values = []
            next_layer_nodes = []

            # Iterate through all nodes in current layers
            for node in cur:

                # Check if a node is not none
                if node:

                    # Add values of current node into list
                    cur_layer_values.append(node.val)

                    # Add childrens of current node into next_layer_nodes
                    next_layer_nodes.extend([node.left, node.right])

            # If after for loop, we have got some values in list, then insert this list into queue
            if cur_layer_values:
                queue.insert(0, cur_layer_values)

            # Update cur list to next_layer_nodes, to repeat above process to the next layer of nodes
            cur = next_layer_nodes
        return queue
