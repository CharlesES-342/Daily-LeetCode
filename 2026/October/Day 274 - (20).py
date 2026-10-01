# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Example 5:
# Input: s = "([)]"
# Output: false

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'

class Solution(object):

    def isValid(self, s):
        """

        :type s: str

        :rtype: bool

        """
        bracketStack = []

        for char in s:
            # Push opening brackets onto the stack
            if char in "([{":
                bracketStack.append(char)
            else:
                # If stack is empty it's invalid (given an opening exists)
                if not bracketStack:
                    return False

                curr = bracketStack.pop()

                # Ensure matching types
                if (
                    (char == ")" and curr != "(")
                    or (char == "}" and curr != "{")
                    or (char == "]" and curr != "[")
                ):
                    return False

        # Valid only if all brackets were closed (stack is empty)
        return len(bracketStack) == 0