# 3090. Maximum Length Substring With Two Occurrences

# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.

# Example 1:
# Input: s = "bcbbbcba"
# Output: 4
# Explanation:
# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

# Example 2:
# Input: s = "aaaa"
# Output: 2
# Explanation:
# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".

# Constraints:
# 2 <= s.length <= 100
# s consists only of lowercase English letters.

class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = defaultdict(int)
        start = 0
        max_length = 0
        k = 2
        
        for end in range(len(s)):
            curr = s[end]
            count[curr] += 1
            
            # if count exceeds k move left until its valid again
            while count[curr] > k:
                count[s[start]] -= 1
                start += 1
                
            max_length = max(max_length, end - start + 1)
            
        return max_length
        

'''
Code repurposed from
Day 224 - 2958. Length of Longest Subarray With at Most K Frequency
'''