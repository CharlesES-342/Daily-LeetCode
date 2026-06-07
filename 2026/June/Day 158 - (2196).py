# 2196. Create Binary Tree From Descriptions

# You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,
# If isLefti == 1, then childi is the left child of parenti.
# If isLefti == 0, then childi is the right child of parenti.
# Construct the binary tree described by descriptions and return its root.
# The test cases will be generated such that the binary tree is valid.

# Example 1:
# Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# Output: [50,20,80,15,17,19]
# Explanation: The root node is the node with value 50 since it has no parent.
# The resulting binary tree is shown in the diagram.

# Example 2:
# Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
# Output: [1,2,null,null,3,4]
# Explanation: The root node is the node with value 1 since it has no parent.
# The resulting binary tree is shown in the diagram.

# Constraints:
# 1 <= descriptions.length <= 104
# descriptions[i].length == 3
# 1 <= parenti, childi <= 105
# 0 <= isLefti <= 1
# The binary tree described by descriptions is valid.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        nodes = {}
        children = set()
        
        for parent_val, child_val, is_left in descriptions:
            # Create the parent node if we haven't seen it yet
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
                
            # Create the child node if we haven't seen it yet
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)
                
            # Link the child to the parent
            if is_left == 1:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]
                
            # Mark this node as a child
            children.add(child_val)
            
        # The root is the node that is not in the children set
        for node_val in nodes:
            if node_val not in children:
                return nodes[node_val]
                
        return None