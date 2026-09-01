# 3568. Minimum Moves to Clean the Classroom

# You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:
# 'S': Starting position of the student
# 'L': Litter that must be collected (once collected, the cell becomes empty)
# 'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
# 'X': Obstacle the student cannot pass through
# '.': Empty space
# You are also given an integer energy, representing the student's maximum energy capacity. The student starts with this energy from the starting position 'S'.
# Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area 'R', which resets the energy to its maximum capacity energy.
# Return the minimum number of moves required to collect all litter items, or -1 if it's impossible.

# Example 1:
# Input: classroom = ["S.", "XL"], energy = 2
# Output: 2
# Explanation:
# The student starts at cell (0, 0) with 2 units of energy.
# Since cell (1, 0) contains an obstacle 'X', the student cannot move directly downward.
# A valid sequence of moves to collect all litter is as follows:
# Move 1: From (0, 0) → (0, 1) with 1 unit of energy and 1 unit remaining.
# Move 2: From (0, 1) → (1, 1) to collect the litter 'L'.
# The student collects all the litter using 2 moves. Thus, the output is 2.

# Example 2:
# Input: classroom = ["LS", "RL"], energy = 4
# Output: 3
# Explanation:
# The student starts at cell (0, 1) with 4 units of energy.
# A valid sequence of moves to collect all litter is as follows:
# Move 1: From (0, 1) → (0, 0) to collect the first litter 'L' with 1 unit of energy used and 3 units remaining.
# Move 2: From (0, 0) → (1, 0) to 'R' to reset and restore energy back to 4.
# Move 3: From (1, 0) → (1, 1) to collect the second litter 'L'.
# The student collects all the litter using 3 moves. Thus, the output is 3.

# Example 3:
# Input: classroom = ["L.S", "RXL"], energy = 3
# Output: -1
# Explanation:
# No valid path collects all 'L'.

# Constraints:
# 1 <= m == classroom.length <= 20
# 1 <= n == classroom[i].length <= 20

class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        m, n = len(classroom), len(classroom[0])
        
        # Locate 'S', count and index 'L's
        litter_coords = []
        start_x, start_y = 0, 0
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_x, start_y = r, c
                elif classroom[r][c] == 'L':
                    litter_coords.append((r, c))
                    
        total_litter = len(litter_coords)
        litter_map = {coord: i for i, coord in enumerate(litter_coords)}
        
        target_mask = (1 << total_litter) - 1
        
        # Queue stores: (x, y, mask, current_energy, steps)
        queue = deque([(start_x, start_y, 0, energy, 0)])
        
        # best_energy[x][y][mask] stores the max energy we've had at this state
        best_energy = {}
        best_energy[(start_x, start_y, 0)] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # possible movements
        
        while queue: # for each location/classroom location
            x, y, mask, curr_e, steps = queue.popleft()
            
            if mask == target_mask:
                return steps
                
            for dx, dy in directions: # for all dirrecttion movements
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                    next_e = curr_e - 1
                    if next_e < 0:
                        continue
                        
                    next_mask = mask
                    cell = classroom[nx][ny]
                    
                    if cell == 'L':
                        l_idx = litter_map[(nx, ny)]
                        next_mask |= (1 << l_idx)
                        
                    if cell == 'R':
                        next_e = energy
                        
                    # Check if this state has been visited with strictly more energy
                    state_key = (nx, ny, next_mask)
                    if best_energy.get(state_key, -1) < next_e:
                        best_energy[state_key] = next_e
                        queue.append((nx, ny, next_mask, next_e, steps + 1))
                        
        return -1


'''
Locate the start (S)
Locate the litter and add it to a bitwise list where each piece of litter (each location) corresponds
to a bit in the bitwise list.

Then travel through as BFS (Breadth First Search) where each state is defined by the current
position, the bitwise mask of collected litter, and the current energy level.
for each location, apply all possible movementts that are possible (adding them to the list). With
each movement, check if the move is valid or if the energy is depleted. If the move is valid,
update the bitwise mask if litter is collected and reset energy if on a reset area (R).
In doing so, check the energy level and the bitwise mask to see if this state has been visited
with more energy. If not, this is the new most efficient state.
'''