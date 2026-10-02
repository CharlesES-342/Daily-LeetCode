# 22. Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]

# Constraints:
# 1 <= n <= 8

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # all combinations
        # for all spaces, it can either have a close or open bracket (taking 1 form the count)
        res = []
        
        def backtrack(curr_str, open_count, close_count):
            # valid string formed
            if len(curr_str) == 2*n:
                res.append(curr_str)
                return
            
            # 1. add an open (
            if open_count < n:
                backtrack(curr_str + '(', open_count + 1, close_count)
            # 2. add a close (
            if close_count < open_count: #if n i used it allows for all combinations off the (valid or not)
                backtrack(curr_str + ')', open_count, close_count + 1)

        backtrack('', 0, 0)
        return res

'''
Initially, I used 'close_count < n' on line 6, forgetting that valid strings are required, not all possible
combinations.
'''