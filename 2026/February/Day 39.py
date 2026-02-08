# 110. Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.


# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true


# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

class Solution(object):
    def isBalanced(self, root):
        #calculate height of a tree
        def getHeight(node):
            if not node:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        #check recursively if all of the left and right subtrees are balanced, and then add itself (to then move back up the recursion to teh root)
        if not root:
            return True  # Empty tree is balanced
        
        #if an indicvidual node is not banalced, then teh enire thing will also not be balanced
        #check left subtree is balanced
        if not self.isBalanced(root.left):
            return False
        #check right subtree is balanced
        if not self.isBalanced(root.right):
            return False
        
        #check current node is balanced
        left_height = getHeight(root.left)
        right_height = getHeight(root.right)
        
        #if not balanced
        if abs(left_height - right_height) > 1: 
            return False
        
        return True