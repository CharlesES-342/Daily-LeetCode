#85. Maximal Rectangle

# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.


# Example 1:
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.

# Example 2:
# Input: matrix = [["0"]]
# Output: 0

# Example 3:
# Input: matrix = [["1"]]
# Output: 1

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        #edge case - if matrix is empty
        if not matrix or not matrix[0]:
            return 0
        
        max_area = 0
        rows, cols = len(matrix), len(matrix[0])

        #create a heights array to store the height of 1's for each column
        heights = [0] * cols
        for r in range(rows):
            for c in range(cols):
                #update the heights array
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            
            #calculate the maximum area for the current row's histogram
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area
    
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        max_area = 0
        heights.append(0)  # Append a sentinel value to pop all remaining bars in stack
        #for all the heights, calculate the maximum area
        # for every column, determine how far left and right we can extend the rectangle and calculate area
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1 #if stack is empty, width is i, else width is distance between current index and index of last element in stack - 1
                max_area = max(max_area, h * w) #calculate area - also includes the case where stack is empty (finds the max to ensure correctness)
            stack.append(i)
        heights.pop()  # Remove the sentinel value
        return max_area