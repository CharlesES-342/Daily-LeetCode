# 3666. Minimum Operations to Equalize Binary String

# You are given a binary string s, and an integer k.
# In one operation, you must choose exactly k different indices and flip each '0' to '1' and each '1' to '0'.
# Return the minimum number of operations required to make all characters in the string equal to '1'. If it is not possible, return -1.

# Example 1:
# Input: s = "110", k = 1
# Output: 1
# Explanation:
# There is one '0' in s.
# Since k = 1, we can flip it directly in one operation.

# Example 2:
# Input: s = "0101", k = 3
# Output: 2
# Explanation:
# One optimal set of operations choosing k = 3 indices in each operation is:
# Operation 1: Flip indices [0, 1, 3]. s changes from "0101" to "1000".
# Operation 2: Flip indices [1, 2, 3]. s changes from "1000" to "1111".
# Thus, the minimum number of operations is 2.

# Example 3:
# Input: s = "101", k = 2
# Output: -1
# Explanation:
# Since k = 2 and s has only one '0', it is impossible to flip exactly k indices to make all '1'. Hence, the answer is -1.

# Constraints:
# 1 <= s.length <= 10​​​​​​​5
# s[i] is either '0' or '1'.
# 1 <= k <= s.length

'''
First Approach: this took too long to run
'''
from collections import deque
class Solution(object):
    def minOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len (s)
        zeroCount = s.count('0')
        #for preventing loops
        visited = {zeroCount}

        #base case - already sorted
        if zeroCount == 0 :
            return 0

        #go though by BFS to find where this value is 0 for number of zeros
        queue = deque([(zeroCount, 0)])
        
        while queue:
            #get the current position you are looking at (number of zeros, distance from the root)
            #where the distnace from teh root is eqal to the number of operations
            currentCount, dist = queue.popleft() 

            #you are choosing some k zeros from s:
            #   this cant exceed the number of 0's we have and not more than the number of elements
            #the range of x chosen:
            min_x = max(0, k - (n - currentCount))
            max_x = min(k, currentCount)
            #if this x < k, then some ones are also changed to 0's
            #   therefor: 0's count = (count-x) + (k + (count-x)

            #following each operation, the net change is equivilent to (k-2x)
            for x in range(min_x, max_x + 1):
                nextCount = currentCount + k - 2 * x
                #ending condition - the result is complete
                if nextCount == 0: 
                    return dist + 1 #the next level that is a success

                #check if visited
                if nextCount not in visited:
                    visited.add(nextCount)
                    queue.append((nextCount, dist+1))
            
            #if this all fails and you go through the intire list of possible swap valies and still cant get an answer (you get to a previously visited number of 0's - stop so you dont enter an infinite loop)
        return -1
        

'''
This approach now makes use of the 3rd Hint. This improves the time complexity from O(n * k) to O(n log n)
This approach uses parity to skip over numbers we know we cant get to. For example, if k is odd, then we can only get to even numbers of 0's. If k is even, then we can only get to odd numbers of 0's.
This is because the net change in the number of 0's is always k - 2x, which has the same parity as k.
'''
from collections import deque

class Solution(object):
    def minOperations(self, s, k):
        n = len(s)
        z = s.count('0')
        if z == 0: return 0
        
        # Hint 3: Separate unvisited nodes by parity
        unvisited = [set(), set()]
        for i in range(n + 1):
            if i != z:
                unvisited[i % 2].add(i)
        
        queue = deque([(z, 0)])
        
        while queue:
            curr_z, dist = queue.popleft()
            
            # Calculate the range of next_z reachable from curr_z
            # Min next_z occurs when we flip as many zeros as possible (max_x)
            # Max next_z occurs when we flip as many ones as possible (min_x)
            min_x = max(0, k - (n - curr_z))
            max_x = min(k, curr_z)
            
            lo = curr_z + k - 2 * max_x
            hi = curr_z + k - 2 * min_x
            parity = lo % 2
            
            # Hint 3: Instead of a full loop, only visit what's left in the range
            # In a real O(n log n) solution, we'd use a SortedList and slice the range.
            # In Python, we can iterate over a copy of the set and remove elements.
            to_remove = [v for v in unvisited[parity] if lo <= v <= hi]
            
            for next_z in to_remove:
                if next_z == 0: return dist + 1
                queue.append((next_z, dist + 1))
                unvisited[parity].remove(next_z)
                
        return -1

'''
Approach 3, using the Editorial
'''
from collections import deque
import bisect

class Solution(object):
    def minOperations(self, s, k):
        n = len(s)
        initial_zeros = s.count('0')
        if initial_zeros == 0:
            return 0
        
        # Two sorted lists of unvisited states: one for even counts, one for odd
        unvisited = [[], []]
        for i in range(n + 1):
            if i != initial_zeros:
                unvisited[i % 2].append(i)
        
        # dist[i] stores the min operations to reach i zeros
        # We use a queue for BFS: (current_zeros, current_distance)
        queue = deque([(initial_zeros, 0)])
        
        while queue:
            m, d = queue.popleft()
            
            # Editorial formulas for c1 and c2
            c1 = max(k - n + m, 0)
            c2 = min(m, k)
            
            # Editorial formulas for l_node and r_node
            # l_node: flipping as many zeros as possible (c2)
            # r_node: flipping as few zeros as possible (c1)
            l_node = m + k - 2 * c2
            r_node = m + k - 2 * c1
            
            # The parity of all reachable states from m
            p = l_node % 2
            target_list = unvisited[p]
            
            # Use binary search (bisect) to find the range [l_node, r_node] 
            # in our unvisited list
            left_idx = bisect.bisect_left(target_list, l_node)
            right_idx = bisect.bisect_right(target_list, r_node)
            
            # Collect all unvisited states in this range
            found_states = target_list[left_idx : right_idx]
            
            for next_m in found_states:
                if next_m == 0:
                    return d + 1
                queue.append((next_m, d + 1))
            
            # Crucial optimization: Delete these states so we never look at them again
            # This turns the complexity from O(N*K) to near O(N)
            del target_list[left_idx : right_idx]
                
        return -1
    
    #====== HOW IT WORKS ======
    #taking the same approaches as the other methods to take the intial count of 0's
    #then we have two lists of unvisited states, one for even counts and one for odd counts
    #we use a queue for BFS, starting with the initial count of 0's and distance 0
    #for each state, we calculate the range of next states we can reach by flipping k bits
    #we use binary search to find the indices of the unvisited states in this range
    #we add these states to the queue and delete them from the unvisited list to avoid revisiting them
    #if we reach a state with 0 zeros, we return the distance + 1 as the answer - else return -1 if all
    # possibilities have been exhausted and it is not possible to reach 0 zeros.