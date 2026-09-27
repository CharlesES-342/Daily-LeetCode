# 1190. Reverse Substrings Between Each Pair of Parentheses

# You are given a string s that consists of lower case English letters and brackets.
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
# Your result should not contain any brackets.

# Example 1:
# Input: s = "(abcd)"
# Output: "dcba"

# Example 2:
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.

# Example 3:
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

# Constraints:
# 1 <= s.length <= 2000
# s only contains lower case English characters and parentheses.
# It is guaranteed that all parentheses are balanced.

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        # since brackes can be inside others you can either:
        # 1. count the depth and swap if it is an even depth
        # 2. att every bracket, find all matching pairs and filp the sections that way using recursion
        # the order of the swaps does not matter
        
        n = len(s)
        pair = {}
        stack = []

        # Map matching parentheses indices
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        # Traverse with directional steps
        res = []
        i = 0
        direction = 1

        while i < n:
            if s[i] in "()": # if a baracet, swap direction of rotation between this and next index of rotation
                i = pair[i]
                direction = -direction
            else:
                res.append(s[i])
            i += direction

        return "".join(res) 

'''
This O(n) method was helkped to be inderstood by gemini.ai. Initial;lt, my method would have taken slightly longer in time complexity
as the re-aranging wasnt quite as efficicnent and I was swapping the wrong indexes (like a fool). FOllowing this, I gave my code to
gemini, and it corrected my code and made a few other alterations to remove some unecessary porocessing regarding what needed to be
swapped when to streamline my solution.
'''