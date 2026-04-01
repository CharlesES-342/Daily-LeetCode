# 2751. Robot Collisions

# There are n 1-indexed robots, each having a position on a line, health, and movement direction.
# You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.
# All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.
# If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.
# Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final health of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.
# Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.
# Note: The positions may be unsorted.

# Example 1:
# Input: positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"
# Output: [2,17,9,15,10]
# Explanation: No collision occurs in this example, since all robots are moving in the same direction. So, the health of the robots in order from the first robot is returned, [2, 17, 9, 15, 10].

# Example 2:
# Input: positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"
# Output: [14]
# Explanation: There are 2 collisions in this example. Firstly, robot 1 and robot 2 will collide, and since both have the same health, they will be removed from the line. Next, robot 3 and robot 4 will collide and since robot 4's health is smaller, it gets removed, and robot 3's health becomes 15 - 1 = 14. Only robot 3 remains, so we return [14].

# Example 3:
# Input: positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL"
# Output: []
# Explanation: Robot 1 and robot 2 will collide and since both have the same health, they are both removed. Robot 3 and 4 will collide and since both have the same health, they are both removed. So, we return an empty array, [].

# Constraints:
# 1 <= positions.length == healths.length == directions.length == n <= 105
# 1 <= positions[i], healths[i] <= 109
# directions[i] == 'L' or directions[i] == 'R'
# All values in positions are distinct

class Solution(object):
    def survivedRobotsHealths(self, positions, healths, directions):
        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """
        n = len(positions)
        # index array and sort it based on positions
        indices = sorted(range(n), key=lambda i: positions[i])
        
        stack = []  # To store indices of robots moving Right ('R')

        #iterate steps
        for i in indices:
            if directions[i] == 'R':
                stack.append(i)
            else: #moving left
                while stack and healths[i] > 0:
                    top_idx = stack[-1]

                    if healths[i]>healths[top_idx]:
                        # left wins the contact (left -1, right dies)
                        healths[top_idx] = 0
                        healths[i] -= 1
                        stack.pop()
                    elif healths[i] < healths[top_idx]:
                        # right wins contact (let dead, right -1)
                        healths[i] = 0
                        healths[top_idx] -= 1
                    else:
                        # both robots die
                        healths[i] = 0
                        healths[top_idx] = 0
                        stack.pop()

        #return all the healths                
        return [h for h in healths if h > 0]
    
#for a hard problem, i was confused by why it was so simple
#   simply move through the positions and take a step and then return the values after collisions are prevented
#   intially i thought this was a 3D space problem, but I was wrong, they simply move over one single line
#   one of the key parts is that you dont need to know the number of stteps taken (so you can just compute collisions of a robot
#   and move over the positions in its path and the robots you will collide with)