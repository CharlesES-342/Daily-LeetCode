# 3336. Find the Number of Subsequences With Equal GCD

# You are given an integer array nums.
# Your task is to find the number of pairs of non-empty subsequences (seq1, seq2) of nums that satisfy the following conditions:
# The subsequences seq1 and seq2 are disjoint, meaning no index of nums is common between them.
# The GCD of the elements of seq1 is equal to the GCD of the elements of seq2.
# Return the total number of such pairs.
# Since the answer may be very large, return it modulo 109 + 7.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: 10
# Explanation:
# The subsequence pairs which have the GCD of their elements equal to 1 are:
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])
# ([1, 2, 3, 4], [1, 2, 3, 4])

# Example 2:
# Input: nums = [10,20,30]
# Output: 2
# Explanation:
# The subsequence pairs which have the GCD of their elements equal to 10 are:
# ([10, 20, 30], [10, 20, 30])
# ([10, 20, 30], [10, 20, 30])

# Example 3:
# Input: nums = [1,1,1,1]
# Output: 50

# Constraints:
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 200

'''Initial Porcess'''
class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Euclidean Algorithm for GCD
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # For each value in the sequence, it can be added to:
        #   sequence 1
        #   sequence 2
        #   or it can be skipped (not added to either sequence)

        # Form a DP table to generate each possible sequence and the GCD from it
        n = len(nums)
        
        def dp(i, x, y):
            # Base Case: We've made a decision for every element
            if i == n:
                # Both subsequences must be non-empty (GCD > 0) and equal
                return 1 if (x > 0 and x == y) else 0
            
            # Option 1: Skip current number
            res = dp(i + 1, x, y)
            
            # Option 2: Put in seq1
            # Our custom gcd(0, val) automatically returns val
            res = (res + dp(i + 1, gcd(x, nums[i]), y)) % MOD
            
            # Option 3: Put in seq2
            res = (res + dp(i + 1, x, gcd(y, nums[i]))) % MOD
            
            return res
        
        # Start at index 0, with both subsequences initially empty (GCD = 0)
        return dp(0, 0, 0)
    
'''
Following the recursion issues, I asked Gemini to complete this before my laptop died:
'''
class Solution(object):
    def subsequencePairCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        max_val = max(nums)
        
        # Custom Euclidean Algorithm for GCD
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # For each value in the sequence, it can be added to:
        #   sequence 1
        #   sequence 2
        #   or it can be skipped (not added to either sequence)

        # Form a DP table to generate each possible sequence and the GCD from it
        # dp[x][y] stores the number of subsequence pairs with GCDs x and y
        dp = [[0] * (max_val + 1) for _ in range(max_val + 1)]
        
        # Base case: 1 way to have both subsequences empty (GCD = 0)
        dp[0][0] = 1

        for num in nums:
            # We construct a new DP state array for this step
            next_dp = [[0] * (max_val + 1) for _ in range(max_val + 1)]
            
            for x in range(max_val + 1):
                for y in range(max_val + 1):
                    if dp[x][y] == 0:
                        continue
                    
                    count = dp[x][y]
                    
                    # Option 1: Skip current number (keep the exact same GCDs)
                    next_dp[x][y] = (next_dp[x][y] + count) % MOD
                    
                    # Option 2: Put in seq1
                    g1 = gcd(x, num)
                    next_dp[g1][y] = (next_dp[g1][y] + count) % MOD
                    
                    # Option 3: Put in seq2
                    g2 = gcd(x, num) # Note: we apply gcd to y
                    g2 = gcd(y, num)
                    next_dp[x][g2] = (next_dp[x][g2] + count) % MOD
            
            dp = next_dp

        # Collect the answer where both subsequences are non-empty (GCD > 0) and equal (x == y)
        ans = 0
        for g in range(1, max_val + 1):
            ans = (ans + dp[g][g]) % MOD

        return ans