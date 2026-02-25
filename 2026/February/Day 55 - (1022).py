# 1022. Sum of Root To Leaf Binary Numbers

# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path
# represents a binary number starting with the most significant bit. For example, if the path is
# 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13. For all leaves in
# the tree, consider the numbers represented by the path from the root to that leaf. Return the sum
# of these numbers. The test cases are generated so that the answer fits in a 32-bits integer.

# Example 1:
# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

# Example 2:
# Input: root = [0]
# Output: 0


# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# Node.val is 0 or 1.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #by doing a depthfirst search, adding the value of a node (from the leaf) to a total
        #do this recursively, working back up the tree
        def dfs(node, current_val):
            if not node:
                return 0
            
            #perform a shift so that the current binary value is in the correct location and then add the current value
            current_val = (current_val << 1) | node.val
            
            #if it's a leaf, return the accumulated path value
            if not node.left and not node.right:
                return current_val
            
            #otherwise, continue down both branches
            return dfs(node.left, current_val) + dfs(node.right, current_val)
        
        return dfs(root, 0)