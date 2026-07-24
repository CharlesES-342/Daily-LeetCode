# 3514. Number of Unique XOR Triplets II

# You are given an integer array nums.
# A XOR triplet is defined as the XOR of three elements nums[i] XOR nums[j] XOR nums[k] where i <= j <= k.
# Return the number of unique XOR triplet values from all possible triplets (i, j, k).

# Example 1:
# Input: nums = [1,3]
# Output: 2
# Explanation:
# The possible XOR triplet values are:
# (0, 0, 0) → 1 XOR 1 XOR 1 = 1
# (0, 0, 1) → 1 XOR 1 XOR 3 = 3
# (0, 1, 1) → 1 XOR 3 XOR 3 = 1
# (1, 1, 1) → 3 XOR 3 XOR 3 = 3
# The unique XOR values are {1, 3}. Thus, the output is 2.

# Example 2:
# Input: nums = [6,7,8,9]
# Output: 4
# Explanation:
# The possible XOR triplet values are {6, 7, 8, 9}. Thus, the output is 4.

# Constraints:
# 1 <= nums.length <= 1500
# 1 <= nums[i] <= 1500

'''
My initial approach wasnt efficient enough in terms of time, despite the pre,computation of the XOR.
This is because the O(n) complexity remained the same
'''

class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # since not all numbers are included, this is harder
        # find the max value possible (the number conmstaining the most high value 1's)
        n = len(nums)
        
        # 1. find all the j and k value pairs, O(n^2)
        #define
        pre_xor = [[0 for _ in range(n)] for _ in range(n)]
        #populate
        for j in range(n):
            for k in range(j,n):
                pre_xor[j][k] = nums[j] ^ nums[k]


        # 2. go thorugh every value of i, determine the new max values, O(n)
        unique_vals = set() # set, only unique values
        for i in range(n):
            for j in range(i, n):
                # nums[i] ^ (nums[j] ^ nums[k]) using our precomputed matrix
                for k in range(j, n):
                    val = nums[i] ^ pre_xor[j][k]
                    unique_vals.add(val)
                    
        return len(unique_vals)


'''
Removing duplicate numbers fromthe array will not work since the location of the numbers is also importaint,
to maintin (i <= j <= k).

Rather than see the combinations, see if a number is possible initially, and then for every possible number (formed from j and k pairs),
go thorugh every i number and see if a new number is formed. 
Complexity - O(n^2)

KEY TAKEAWAYS:
The location of the values in the answer do not matter!
    XOR is both cummulative and associative, and so the order of operations does not matter so any order will result in the same answer, so you can re-arrrange
    i,j & k to fufill the order requirements.
    (I forgot this)
'''

class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max value possible
        max_val = max(nums)
        limit = max_val << 1
        
        # Track which pair XORs are possible
        has_pair = [False] * limit
        for a in nums:
            for b in nums:
                has_pair[a ^ b] = True
                
        # Track final unique triplet XOR values
        unique_triplets = [0] * limit
        for ab in range(limit):
            if has_pair[ab]:
                for c in nums:
                    unique_triplets[ab ^ c] = 1
                    
        return sum(unique_triplets)