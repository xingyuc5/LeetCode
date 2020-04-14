import java.util.List;

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
    public List<Integer> inorderTraversal(TreeNode root) {
        LinkedList<Integer> results = new LinkedList<Integer>();

        traverse(root, results);

        return results;
    }

    public void traverse(TreeNode root, List<Integer> results) {
        if (root == null)
            return;

        if (root.left != null) {
            traverse(root.left, results);
        }
        results.add(root.val);
        if (root.right != null) {
            traverse(root.right, results);
        }
    }
}