import java.util.LinkedList;
import java.util.List;
import java.util.Stack;
import java.util.Math;

// Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

class Solution {
    public boolean isBalanced(TreeNode root) {

        if (root == null)
            return true;
        // a tree is balanced if left subtree is balanced
        // right subtree is balanced
        // diff in height differs from no more than 1
        return isBalanced(root.left) && isBalanced(root.right) && Math.abs(height(root.left) - height(root.right)) <= 1;

    }

    public int height(TreeNode root) {
        if (root == null)
            return 0;

        int leftHeight = height(root.left);
        int rightHeight = height(root.right);

        return (leftHeight > rightHeight) ? (leftHeight + 1) : (rightHeight + 1);
    }
}