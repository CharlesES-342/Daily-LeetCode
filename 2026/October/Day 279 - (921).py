# 921. Minimum Add to Make Parentheses Valid

# A parentheses string is valid if and only if:
# It is the empty string,
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
# You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.
# For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.

# Example 1:
# Input: s = "())"
# Output: 1

# Example 2:
# Input: s = "((("
# Output: 3

# Constraints:
# 1 <= s.length <= 1000
# s[i] is either '(' or ')'.

'''
My initial though processs was to coun the number of ')' and '(' and then find the difference
between them. However, this approach does not work for all cases as the counts may be corect, but the 
string can be unvalid E.G. '))((', there are 2 of each type but you need 4 to make the string valid.

The following takes into aqccount the order of the brackets and counts openings which are never
closed and closed brackets which are never opened. The exact structure is not needed, only that there is a
matchin number in the correct order of '(' and then ')'
'''

class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        # go through and see how many are poened and enver closed (and how many are closed but never opened)
        opened = 0
        closed = 0
        # by moving forward throguh the array we conclude that a closing bracket will require previous opening and all openeing can only have a closing bracket occure later in the string (to make it valid)
        for i in s:
            if i == '(':
                opened += 1
            else:
                if opened > 0: # if there is a matchin close a bracket pair can be closed
                    opened -= 1
                else: # else, this bracket requires an opener (+1 operation)
                    closed += 1
        
        # whatever is left from opening and closing, these all require operations to close
        return opened + closed
        