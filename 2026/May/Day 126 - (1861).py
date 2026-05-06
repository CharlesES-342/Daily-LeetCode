# 1861. Rotating the Box

# You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

# A stone '#'
# A stationary obstacle '*'
# Empty '.'
# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.
# It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.
# Return an n x m matrix representing the box after the rotation described above.

# Example 1:
# Input: boxGrid = [["#",".","#"]]
# Output: [["."],
#          ["#"],
#          ["#"]]

# Example 2:
# Input: boxGrid = [["#",".","*","."],
#               ["#","#","*","."]]
# Output: [["#","."],
#          ["#","#"],
#          ["*","*"],
#          [".","."]]

# Example 3:
# Input: boxGrid = [["#","#","*",".","*","."],
#               ["#","#","#","*",".","."],
#               ["#","#","#",".","#","."]]
# Output: [[".","#","#"],
#          [".","#","#"],
#          ["#","#","*"],
#          ["#","*","."],
#          ["#",".","*"],
#          ["#",".","."]]

# Constraints:
# m == boxGrid.length
# n == boxGrid[i].length
# 1 <= m, n <= 500
# boxGrid[i][j] is either '#', '*', or '.'.

class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        # reverse(left right) of the transpose, and then move the white spaces

        ROWS = len(boxGrid)
        COLS = len(boxGrid[0])

        # rotate the grid 90 degrees clockwise
        res = [["" for _ in range(ROWS)] for _ in range(COLS)]
        for r in range(ROWS):
            for c in range(COLS):
                res[c][ROWS - 1 - r] = boxGrid[r][c]

        # apply gravity (stones '#' fall down toward the bottom of 'res')
        R, C = COLS, ROWS
        
        for c in range(C):
            # track the lowest available empty slot in the current column
            lowest_empty = R - 1
            for r in range(R - 1, -1, -1):
                if res[r][c] == '#':
                    # swap stone to the lowest empty position
                    res[r][c], res[lowest_empty][c] = res[lowest_empty][c], res[r][c]
                    lowest_empty -= 1
                elif res[r][c] == '*':
                    # Obstacle blocks. new lowest_empty
                    lowest_empty = r - 1
                # If it's a '.', we just leave lowest_empty where it is

        return res