#1161. Max Level SUm of a Binary Tree

# Given the root of a binary tree, return the smallest level X such that the sum
# of all the values of nodes at level X is maximal.

# Example 1:
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2




#method 1:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = [(root, 1)]  # (node, level)
        level_sums = {}
        max_sum = float('-inf')
        min_level = float('inf')

        while queue:
            node, level = queue.pop(0)

            if node:
                # Update the sum for the current level
                if level not in level_sums:
                    level_sums[level] = 0
                level_sums[level] += node.val

                # Enqueue left and right children with incremented level
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        
        # Find the level with the maximum sum
        for level, total in level_sums.items():
            if total > max_sum or (total == max_sum and level < min_level):
                max_sum = total
                min_level = level
        return min_level
    


#attempt 2 - similar to above but using deque for BFS
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        from collections import deque

        if not root:
            return 0

        queue = deque([root])
        level = 0
        max_sum = float('-inf')
        result_level = 0

        while queue:
            level += 1
            level_size = len(queue)
            current_level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                current_level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if current_level_sum > max_sum:
                max_sum = current_level_sum
                result_level = level
        return result_level