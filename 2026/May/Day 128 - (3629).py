# 3629. Minimum Jumps to Reach End via Prime Teleportation

# You are given an integer array nums of length n.
# You start at index 0, and your goal is to reach index n - 1.
# From any index i, you may perform one of the following operations:
# Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
# Prime Teleportation: If nums[i] is a prime number p, you may instantly jump to any index j != i such that nums[j] % p == 0.
# Return the minimum number of jumps required to reach index n - 1.

# Example 1:
# Input: nums = [1,2,4,6]
# Output: 2
# Explanation:
# One optimal sequence of jumps is:
# Start at index i = 0. Take an adjacent step to index 1.
# At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.
# Thus, the answer is 2.

# Example 2:
# Input: nums = [2,3,4,7,9]
# Output: 2
# Explanation:
# One optimal sequence of jumps is:
# Start at index i = 0. Take an adjacent step to index i = 1.
# At index i = 1, nums[1] = 3 is a prime number. Therefore, we teleport to index i = 4 since nums[4] = 9 is divisible by 3.
# Thus, the answer is 2.

# Example 3:
# Input: nums = [4,6,5,8]
# Output: 3
# Explanation:
# Since no teleportation is possible, we move through 0 → 1 → 2 → 3. Thus, the answer is 3.

# Constraints:
# 1 <= n == nums.length <= 105
# 1 <= nums[i] <= 106

class Solution(object):
    def minJumps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # it may be adventageious to jump back 10 to got fromard 100 for example
        # For Each position, what is the furthest ahead multiple of P you can get to
        # 1. identify the primes (p) in nums
        # 2. for each p, identify multiples, nums[j] % p == 0
        # 3. using BFS move check each position available (use a queue)
        # 4. first to get to the end (n-1) is the winning nuber of jumps - as it has minimum depth
        n = len(nums)
        if n <= 1:
            return 0
        
        max_val = max(nums)
        
        # 1. Identify primes up to max(nums)
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(max_val**0.5) + 1):
            if is_prime[p]:
                is_prime[p*p : max_val+1 : p] = [False] * len(range(p*p, max_val+1, p))
        
        # 2. Map every value in nums to the indices where it appears
        # This allows us to find all multiples (nums[j] % p == 0) efficiently
        val_to_indices = collections.defaultdict(list)
        for i, val in enumerate(nums):
            val_to_indices[val].append(i)
        
        # 3. BFS setup
        queue = collections.deque([(0, 0)])  # (current_index, jump_count)
        visited_indices = [False] * n
        visited_indices[0] = True
        
        # Track which primes we have already used for teleportation
        used_primes = [False] * (max_val + 1)
        
        while queue:
            curr, dist = queue.popleft()
            
            # Check if we have reached the destination
            if curr == n - 1:
                return dist
            
            # --- Move 1: Adjacent Steps ---
            # if a valid position and not perviouslly visted (if previously visited, it cant give a solution greater than the current optimum)
            for next_idx in (curr - 1, curr + 1):
                if 0 <= next_idx < n and not visited_indices[next_idx]:
                    visited_indices[next_idx] = True
                    queue.append((next_idx, dist + 1))
            
            # --- Move 2: Prime Teleportation ---
            p = nums[curr]
            # Check if current value is prime and we haven't exhausted this prime yet
            if p <= max_val and is_prime[p] and not used_primes[p]:
                used_primes[p] = True
                
                # Identify all multiples of p that exist in the nums array
                for multiple in range(p, max_val + 1, p):
                    if multiple in val_to_indices:
                        # Add all indices containing this multiple to the queue
                        for idx in val_to_indices[multiple]:
                            if not visited_indices[idx]:
                                visited_indices[idx] = True
                                queue.append((idx, dist + 1))
                        
                        # Optimisation: Once these indices are visited, 
                        # we never need to check this specific multiple again.
                        del val_to_indices[multiple]
        
        return -1 # Return -1 if the end is unreachable