# 1386. Cinema Seat Allocation

# A cinema has n rows of seats, numbered from 1 to n. Each row has 10 seats, numbered from 1 to 10.
# You are given a 2D integer array reservedSeats, where reservedSeats[i] = [rowi, seati] means that seat seati in row rowi is already reserved.
# A four-person group must be assigned to four seats in the same row. The group can be seated in one of the following seat blocks:
# seats 2, 3, 4, 5
# seats 4, 5, 6, 7
# seats 6, 7, 8, 9
# A block can be used only if none of its seats are reserved. Each seat can be assigned to at most one group.
# Return an integer denoting the maximum number of four-person groups that can be assigned.

# Example 1:
# Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
# Output: 4
# Explanation: The figure above shows an optimal allocation of four groups. Seats marked in blue are already reserved, and each set of four contiguous seats marked in orange is assigned to one group.

# Example 2:
# Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
# Output: 2

# Example 3:
# Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
# Output: 4

# Constraints:
# 1 <= n <= 109
# 1 <= reservedSeats.length <= min(10 * n, 104)
# reservedSeats[i] == [rowi, seati]
# 1 <= rowi <= n
# 1 <= seati <= 10
# All reservedSeats[i] are distinct.

import collections

class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :type rtype: int
        """
        # Map each row to a set of reserved columns
        row_map = collections.defaultdict(set)
        for row, col in reservedSeats:
            row_map[row].add(col)
            
        # Rows with no reservations can seat 2 families each
        ans = (n - len(row_map)) * 2
        
        for row, reserved in row_map.items():
            left_free = not any(seat in reserved for seat in [2, 3, 4, 5])
            right_free = not any(seat in reserved for seat in [6, 7, 8, 9])
            middle_free = not any(seat in reserved for seat in [4, 5, 6, 7])
            
            if left_free and right_free:
                ans += 2
            elif left_free or right_free or middle_free:
                ans += 1
                
        return ans

'''
This can also be acheived thorugh mapping
'''
class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        # Dictionary to store the reserved seats for each row as a bitmask
        rows = {}
        for r, s in reservedSeats:
            # Set the bit corresponding to the reserved seat
            rows[r] = rows.get(r, 0) | (1 << (s - 1))
            
        # Bitmasks representing the 4-seat blocks (using 0-indexed bit positions):
        # Seats 2-5
        LEFT = 0b0000011110      
        # Seats 4-7
        MIDDLE = 0b0001111000    
        # Seats 6-9
        RIGHT = 0b0111100000     
        
        # Rows with no reserved seats can each fit the maximum of 2 families
        ans = (n - len(rows)) * 2
        
        # Check each row that has at least one reservation
        for mask in rows.values():
            # Check if the left or right 4-seat blocks are completely free
            left = (mask & LEFT) == 0
            right = (mask & RIGHT) == 0
            
            # If both left and right blocks are free, we can seat 2 families
            if left and right:
                ans += 2
            # One of the places is free
            elif left or right or (mask & MIDDLE) == 0:
                ans += 1
                
        return ans