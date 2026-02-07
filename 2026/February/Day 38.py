# 1653. Minimum Deletions to Make String Balanced

# You are given a string s consisting only of characters 'a' and 'b'​​​​.
# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
# Return the minimum number of deletions needed to make s balanced.

# Example 1:
# Input: s = "aababbab"
# Output: 2
# Explanation: You can either:
# Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
# Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

# Example 2:
# Input: s = "bbaaaaabb"
# Output: 2
# Explanation: The only solution is to delete the first two characters.


# Constraints:
# 1 <= s.length <= 105
# s[i] is 'a' or 'b'​​.

import heapq

class Solution(object):
    def minimumDeletions(self, s):
        b_count = 0  # Count of 'b's seen so far
        deletions = 0
        
        for char in s:
            if char == 'b':
                b_count += 1
            else:  # char == 'a'
                # Option 1: Delete this 'a' (deletions + 1)
                # Option 2: Delete all previous 'b's (b_count)
                # Choose minimum
                deletions = min(deletions + 1, b_count)
        
        return deletions 