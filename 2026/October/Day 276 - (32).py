# 32. Longest Valid Parentheses

# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

# Example 1:
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".

# Example 2:
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".

# Example 3:
# Input: s = ""
# Output: 0

# Constraints:
# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        max_len = 0
        
        # for each elemtn, add the element if the next cahracter is valid (if it completes the next string that bracket pair can be removed from the processing). Repeat this until the stack is empty, then record what the previous valid length was. Big O: O(n) as you only look at elements once
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len
