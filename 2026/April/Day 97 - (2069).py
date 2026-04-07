# 2069. Walking Robot Simulation II

# A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions ("North", "East", "South", and "West"). A robot is initially at cell (0, 0) facing direction "East".
# The robot can be instructed to move for a specific number of steps. For each step, it does the following.
# Attempts to move forward one cell in the direction it is facing.
# If the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.
# After the robot finishes moving the number of steps required, it stops and awaits the next instruction.
# Implement the Robot class:
# Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East".
# void step(int num) Instructs the robot to move forward num steps.
# int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].
# String getDir() Returns the current direction of the robot, "North", "East", "South", or "West".

# Example 1:
# Input
# ["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
# [[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
# Output
# [null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]
# Explanation
# Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
# robot.step(2);  // It moves two steps East to (2, 0), and faces East.
# robot.step(2);  // It moves two steps East to (4, 0), and faces East.
# robot.getPos(); // return [4, 0]
# robot.getDir(); // return "East"
# robot.step(2);  // It moves one step East to (5, 0), and faces East.
#                 // Moving the next step East would be out of bounds, so it turns and faces North.
#                 // Then, it moves one step North to (5, 1), and faces North.
# robot.step(1);  // It moves one step North to (5, 2), and faces North (not West).
# robot.step(4);  // Moving the next step North would be out of bounds, so it turns and faces West.
#                 // Then, it moves four steps West to (1, 2), and faces West.
# robot.getPos(); // return [1, 2]
# robot.getDir(); // return "West"

# Constraints:
# 2 <= width, height <= 100
# 1 <= num <= 105
# At most 104 calls in total will be made to step, getPos, and getDir.

class Robot(object):
    DIR_NAMES = ("East", "North", "West", "South")
    DIR_MOVES = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def __init__(self, width, height):
        """
        :type width: int
        :type height: int
        """
        self.width = width
        self.height = height
        # Perimeter of the boundary cells
        self.perimeter = 2 * (width + height) - 4
        self.dir_idx = 0
        self.x = 0
        self.y = 0
        self.has_moved = False # Track if the robot ever moved

    def step(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.has_moved = True
        num %= self.perimeter
        
        # If num is 0 after modulo, it means we completed a full circle.
        # At (0,0), after moving at least one lap, the direction is always South.
        if num == 0 and self.x == 0 and self.y == 0:
            self.dir_idx = 3
            return

        while num > 0:
            dx, dy = self.DIR_MOVES[self.dir_idx]

            if   dx ==  1: steps_to_wall = (self.width  - 1) - self.x
            elif dx == -1: steps_to_wall = self.x
            elif dy ==  1: steps_to_wall = (self.height - 1) - self.y
            else:          steps_to_wall = self.y

            # If we are at a corner and need to turn
            if steps_to_wall == 0:
                self.dir_idx = (self.dir_idx + 1) % 4
                continue

            move = min(num, steps_to_wall)
            self.x += dx * move
            self.y += dy * move
            num -= move
            
            # If we reached a wall exactly, we need to turn for the next step
            if num > 0:
                self.dir_idx = (self.dir_idx + 1) % 4

    def getPos(self):
        """
        :rtype: List[int]
        """
        return [self.x, self.y]

    def getDir(self):
        """
        :rtype: str
        """
        # Special case: If we haven't moved, the direction is "East".
        # If we have moved and are at (0,0), it's "South".
        if self.x == 0 and self.y == 0 and self.has_moved:
            return "South"
        return self.DIR_NAMES[self.dir_idx]
    
    # intially i wanted to just take the modulo of the steps to see if you complete a lap (forgetting that
    # you might be facing the wrong direction when you get there (if you end up not moving), i used gemini.ai
    # to help me realise this and claude.ai to identify areas of improveent as initially, i would recursively
    # call steps (following a turn) to move in that dircetion for x steps, but this resulted in a 
    # Time Limit Exceeded issue. to rectify, it suggested doing the moves in one (which I initially though would
    # be more complex, but it was actually simpler to implement as you just take the modulo)
    # I see why I was wrong