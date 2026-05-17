# 1306. Jump Game III

# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.
# Notice that you can not jump outside of the array at any time.

# Example 1:
# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation: 
# All possible ways to reach at index 3 with value 0 are: 
# index 5 -> index 4 -> index 1 -> index 3 
# index 5 -> index 6 -> index 4 -> index 1 -> index 3 

# Example 2:
# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true 
# Explanation: 
# One possible way to reach at index 3 with value 0 is: 
# index 0 -> index 4 -> index 1 -> index 3

# Example 3:
# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.

# Constraints:
# 1 <= arr.length <= 5 * 104
# 0 <= arr[i] < arr.length
# 0 <= start < arr.length

class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        # BFS to see if it is possible
        # use a queue of all possible positions you can get to, and then add the next jumps. Keep going until there is a 0

        n = len(arr)
        queue = deque([start])
        # Track visited indices to prevent infinite loops
        visited = set([start])
        
        while queue:
            curr = queue.popleft()
            
            # Goal acheived if at a 0 position
            if arr[curr] == 0:
                return True
                
            # 2 possible next moves (+- position)
            left_move = curr - arr[curr]
            right_move = curr + arr[curr]
            
            # check left position (has it been vistited)
            if 0 <= left_move < n and left_move not in visited:
                visited.add(left_move)
                queue.append(left_move)
                
            # check right position (has it been vistited)
            if 0 <= right_move < n and right_move not in visited:
                visited.add(right_move)
                queue.append(right_move)
                
        # if the queue is empty, it is not possible
        return False