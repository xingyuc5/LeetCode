import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

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
    public List<Integer> postorderTraversal(TreeNode root) {
        LinkedList<Integer> results = new LinkedList<Integer>();
        Stack<TreeNode> nodes = new Stack<TreeNode>();

        nodes.push(root);

        while (!nodes.isEmpty()) {
            TreeNode curr = nodes.pop();

            if (curr != null) {

                nodes.push(curr.left);
                nodes.push(curr.right);
                results.add(0, curr.val);
            }
        }
        return results;
    }
}