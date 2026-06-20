# 1840. Maximum Building Height

# You want to build n new buildings in a city. The new buildings will be built in a line and are labeled from 1 to n.
# However, there are city restrictions on the heights of the new buildings:
# The height of each building must be a non-negative integer.
# The height of the first building must be 0.
# The height difference between any two adjacent buildings cannot exceed 1.
# Additionally, there are city restrictions on the maximum height of specific buildings. These restrictions are given as a 2D integer array restrictions where restrictions[i] = [idi, maxHeighti] indicates that building idi must have a height less than or equal to maxHeighti.
# It is guaranteed that each building will appear at most once in restrictions, and building 1 will not be in restrictions.
# Return the maximum possible height of the tallest building.

# Example 1:
# Input: n = 5, restrictions = [[2,1],[4,1]]
# Output: 2
# Explanation: The green area in the image indicates the maximum allowed height for each building.
# We can build the buildings with heights [0,1,2,1,2], and the tallest building has a height of 2.

# Example 2:
# Input: n = 6, restrictions = []
# Output: 5
# Explanation: The green area in the image indicates the maximum allowed height for each building.
# We can build the buildings with heights [0,1,2,3,4,5], and the tallest building has a height of 5.

# Example 3:
# Input: n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
# Output: 5
# Explanation: The green area in the image indicates the maximum allowed height for each building.
# We can build the buildings with heights [0,1,2,3,3,4,4,5,4,3], and the tallest building has a height of 5.

# Constraints:
# 2 <= n <= 109
# 0 <= restrictions.length <= min(n - 1, 105)
# 2 <= idi <= n
# idi is unique.
# 0 <= maxHeighti <= 109

class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        # firts building is 0
        # difference between 2 buildings next to eachother are 1
        # restrictions = [id, max_height]
        # return the max height
        
        # 1. moving from the left (0) find the index of a restiction & find the max height possible between this
        # 2. between restrictions, find the gap and take location(A) + gap/2 as the max height
        # 3. if you are at the end, find hte max height from location(A) + difference to the end
        
        # Base Case: for no restictions
        if not restrictions:
            return n - 1

        max_height = 0 #default

        #sort restrictions based on ID (their location order)
        restrictions.sort(key=lambda x: x[0])
        
        # Some restrictions need to me altered as some restrictions might exceed what is possible inthe sppace and so need to be changed/capped at a more realistic value
        # Pass 1: Left-to-Right
        prev_id, prev_h = 1, 0
        for i in range(len(restrictions)):
            curr_id, curr_h = restrictions[i]
            # Max height is limited by the previous building's height + the distance between them
            curr_h = min(curr_h, prev_h + (curr_id - prev_id))
            restrictions[i][1] = curr_h
            prev_id, prev_h = curr_id, curr_h
            
        # Pass 2: Right-to-Left
        # Restrictions can also be limited by stricter restrictions ahead of them
        next_id, next_h = restrictions[-1][0], restrictions[-1][1]
        for i in range(len(restrictions) - 2, -1, -1):
            curr_id, curr_h = restrictions[i]
            curr_h = min(curr_h, next_h + (next_id - curr_id))
            restrictions[i][1] = curr_h
            next_id, next_h = curr_id, curr_h

        # Initialize max_height with Phase 1 (Building 1 to the first restriction)
        first_id, first_h = restrictions[0]
        max_height = (first_id - 1 + first_h) // 2
        
        # phase 2: between restrictions
        for i in range(1, len(restrictions)):
            prev_id, prev_height = restrictions[i - 1]
            curr_id, curr_height = restrictions[i]
            
            # Determine the new max possible between the locations using the peak formula
            # Peak = (distance + heightA + heightB) // 2
            local_max = ((curr_id - prev_id) + prev_height + curr_height) // 2
            
            max_height = max(max_height, local_max)
        
        # phase 3: between the last restriction and the end
        last_id, last_height = restrictions[-1]
        distance_to_end = n - last_id
        local_max = last_height + distance_to_end
        
        max_height = max(max_height, local_max)
        
        return max_height
    
    '''
    Uses all of my ideas, the only thing that I used Gemini.ai for was verifying my ideas, it just gave me the code
    so I coudl verify. I checked it, it worked, I fixed the comments to make it more clear and show how 
    my ideas were implemented better.
    '''