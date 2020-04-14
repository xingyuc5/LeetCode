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
    public List<Integer> preorderTraversal(TreeNode root) {
        LinkedList<Integer> results = new LinkedList<Integer>();
        Stack<TreeNode> nodes = new Stack<TreeNode>();

        nodes.add(root);

        while (!nodes.isEmpty()) {
            TreeNode curr = nodes.pop();

            if (curr != null) {
                results.add(curr.val);
                nodes.push(curr.right);
                nodes.push(curr.left);
            }
        }

        return results;
    }
}