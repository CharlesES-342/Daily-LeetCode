# 678. Valid Parenthesis String

# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
# The following rules define a valid string:
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "(*)"
# Output: true

# Example 3:
# Input: s = "(*))"
# Output: true

# Example 4:
# Input: s = "("
# Output: false

# Constraints:
# 1 <= s.length <= 100
# s[i] is '(', ')' or '*'.

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # locations of open brackets
        open_stack = []  # Stores indices of '('
        star_stack = []  # Stores indices of '*'

        # 1. Process the string and push indices onto respective stacks
        for i, char in enumerate(s):
            if char == '(':
                open_stack.append(i)
            elif char == '*':
                star_stack.append(i)
            else:  # char == ')'
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        # 2. Match remaining '(' with '*' that appear AFTER them
        while open_stack and star_stack:
            if open_stack[-1] < star_stack[-1]:
                open_stack.pop()
                star_stack.pop()
            else:
                # '(' appears after '*', which cannot be validly closed
                return False

        # If no unmatched '(' remain, the string is valid
        return len(open_stack) == 0

    '''
    Code generated using Gemini.ai to turn my code from yesterdat (Day 276 - (32)) into a solution
    that uses a stack for both the open brackets and the stars.
    '''