# 1382. Balance a Binary Search Tree

# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

# Example 1:
# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

# Example 2:
# Input: root = [2,1,3]
# Output: [2,1,3]

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# 1 <= Node.val <= 105

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # Step 1: Get sorted array via in-order traversal
        def inorder(node, result):
            if not node:
                return
            inorder(node.left, result)   # Visit left subtree
            result.append(node.val)       # Visit root
            inorder(node.right, result)   # Visit right subtree
        
        sorted_vals = []
        inorder(root, sorted_vals)
        
        # Step 2: Reconstruct balanced BST from sorted array
        def build_balanced_bst(arr, start, end):
            if start > end:
                return None
            
            mid = (start + end) // 2
            node = TreeNode(arr[mid])
            node.left = build_balanced_bst(arr, start, mid - 1)
            node.right = build_balanced_bst(arr, mid + 1, end)
            return node
        
        return build_balanced_bst(sorted_vals, 0, len(sorted_vals) - 1)
    
    # recursively build balanced BST from sorted array