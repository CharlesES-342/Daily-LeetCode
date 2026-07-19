# 1081. Smallest Subsequence of Distinct Characters

# Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

# Example 1:
# Input: s = "bcabc"
# Output: "abc"

# Example 2:
# Input: s = "cbacdcbc"
# Output: "acdb"

# Constraints:
# 1 <= s.length <= 1000
# s consists of lowercase English letters.

'''
My inital approach to this problem was wrong, as it made use of grabbing hte first occurences of
characters. This does not fufill the requrirements of the problem, as it does not guarantee that
the subsequence is lexicographically smallest.
An oversight on my part
'''

'''
To rectify this, a stack is used to keep track of the characters in the subsequence.
'''
class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        #set of character last occurences
        last = {} 
        for i in range(len(s)):
            last[s[i]] = i

        #forming the new subsequence
        stack = []
        seen = set()

        for i in range(len(s)):
            ch = s[i]
            if ch in seen: #if it is already in
                continue

            # WHILE the stack is not empty
            #   AND the end of the stack is greater than the current character
            #   AND there are more occurences of this character later on (so it doesnt matter if it is removed at this stage)
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                # remove the element from the subsequence and mark it as not seen
                seen.remove(stack.pop())

            # Add the new character to the Sequence and mark it as seen
            stack.append(ch)
            seen.add(ch)

        return "".join(stack)