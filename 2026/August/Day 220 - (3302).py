# 3302. Find the Lexicographically Smallest Valid Sequence

# You are given two strings word1 and word2.
# A string x is called almost equal to y if you can change at most one character in x to make it identical to y.
# A sequence of indices seq is called valid if:
# The indices are sorted in ascending order.
# Concatenating the characters at these indices in word1 in the same order results in a string that is almost equal to word2.
# Return an array of size word2.length representing the lexicographically smallest valid sequence of indices. If no such sequence of indices exists, return an empty array.
# Note that the answer must represent the lexicographically smallest array, not the corresponding string formed by those indices.

# Example 1:
# Input: word1 = "vbcca", word2 = "abc"
# Output: [0,1,2]
# Explanation:
# The lexicographically smallest valid sequence of indices is [0, 1, 2]:
# Change word1[0] to 'a'.
# word1[1] is already 'b'.
# word1[2] is already 'c'.

# Example 2:
# Input: word1 = "bacdc", word2 = "abc"
# Output: [1,2,4]
# Explanation:
# The lexicographically smallest valid sequence of indices is [1, 2, 4]:
# word1[1] is already 'a'.
# Change word1[2] to 'b'.
# word1[4] is already 'c'.

# Example 3:
# Input: word1 = "aaaaaa", word2 = "aaabc"
# Output: []
# Explanation:
# There is no valid sequence of indices.

# Example 4:
# Input: word1 = "abc", word2 = "ab"
# Output: [0,1]

# Constraints:
# 1 <= word2.length < word1.length <= 3 * 105
# word1 and word2 consist only of lowercase English letters.

class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        len1 = len(word1)
        len2 = len(word2)
        
        # pre-compute last position of each possible character from word2 in word1
        last = [-1] * len2
        n1 = len1 - 1
        n2 = len2 - 1

        while n1 >= 0 and n2 >= 0:
            if word1[n1] == word2[n2]:
                last[n2] = n1
                n2 -= 1
            n1 -= 1

        # form the smallest words
        ans = []
        mismatch_used = False
        j = 0
        
        for i in range(len1):
            if j == len2: # word formed sucessfully with minimum position values
                break
                
            if word1[i] == word2[j]: # direct character match
                ans.append(i)
                j += 1
            elif not mismatch_used: # use free change if remaining word2 can still be matched later
                if j + 1 == len2 or last[j + 1] > i:
                    ans.append(i)
                    mismatch_used = True
                    j += 1

        # check there is a possible answer formed (if not return the default empty case)
        if len(ans) == len2:
            return ans
        return []