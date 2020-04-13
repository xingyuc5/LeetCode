import java.util.LinkedList;
import java.util.List;

//  Definition for a binary tree node. 
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}

//
class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        LinkedList<List<Integer>> results = new LinkedList<List<Integer>>();
        LinkedList<TreeNode> cur_layer_nodes = new LinkedList<TreeNode>();
        cur_layer_nodes.add(root);

        while (!cur_layer_nodes.isEmpty()) {
            LinkedList<Integer> cur_layer_values = new LinkedList<Integer>();
            LinkedList<TreeNode> next_layer_nodes = new LinkedList<TreeNode>();

            for (TreeNode node : cur_layer_nodes) {
                if (node != null) {
                    cur_layer_values.add(node.val);
                    next_layer_nodes.add(node.left);
                    next_layer_nodes.add(node.right);
                }
            }
            if (!cur_layer_values.isEmpty()) {
                results.add(0, cur_layer_values);
            }
            cur_layer_nodes = next_layer_nodes;
        }
        return results;
    }
}