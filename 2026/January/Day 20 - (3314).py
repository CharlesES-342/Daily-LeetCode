# 3314. Construct Array From Bitwise Array 1

# You are given an array nums consisting of n prime integers.
# You need to construct an array ans of length n, such that, for each index i,
# the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i], i.e. ans[i] OR (ans[i] + 1) == nums[i].
# Additionally, you must minimize each value of ans[i] in the resulting array.
# If it is not possible to find such a value for ans[i] that satisfies the condition, then
# set ans[i] = -1.
# I had no idea how to do this question despite its easy difficulty as i had no idea what it 
# was asking

#Confussed by what this is asking

class Solution(object):
    def minBitwiseArray(self, nums):
        ans = []
        for p in nums:
            if p == 2:
                ans.append(-1)
                continue
            
            # Find the first '0' from the right in the binary of p
            # We want to change the '1' just to the right of that '0' to a '0'
            # to minimize the value.
            
            # This bit-trick finds the rightmost string of 1s
            temp = p
            bit = 0
            # Keep shifting until we find the first 0 from the right
            while (temp >> bit) & 1:
                bit += 1
            
            # The bit we want to flip to 0 is (bit - 1)
            # Example: p=7 (111), bit becomes 3. We flip bit (3-1)=2.
            # 7 ^ (1 << 2) = 011 (3).
            res = p ^ (1 << (bit - 1))
            ans.append(res)
            
        return ans