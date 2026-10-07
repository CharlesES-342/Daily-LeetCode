# 301. Remove Invalid Parentheses

# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
# Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

# Example 1:
# Input: s = "()())()"
# Output: ["(())()","()()()"]

# Example 2:
# Input: s = "(a)())()"
# Output: ["(a())()","(a)()()"]

# Example 3:
# Input: s = ")("
# Output: [""]

# Constraints:
# 1 <= s.length <= 25
# s consists of lowercase English letters and parentheses '(' and ')'.
# There will be at most 20 parentheses in s.


'''
Initial Idea:
'''
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # find how many it is invalid by
        # determine if it is because opf troo many open or close brackets
        # remove this number of open/close brackets (from appropriate places), to make it  valid
        #    consider that rmoving one may make it valid again
        
        # Use recursion
        # loop through and for each bracket you can either keep or remove it
        # count the final length differences (once you have every combination). The ones with length closes to the original will be the minimum removed elements and will be part of the answer

        # 1. calculate number of missplaced open and close brackets (this will be a minimum for removal, any more and it wont be a minimum)
        left_rem = 0
        right_rem = 0
        for char in s:
            if char == '(':
                left_rem += 1
            elif char == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        # since an answer MUST be unique, only work in sets (this automatically removes the cases where 2 consecutive characters are the same and either one can be the removed one, and still result in the same resulting stirng)
        result = set()

        # 2. Backtacking and recursion - moving character by character
        def backtrack(index, left_rem, right_rem, open_count, current_path):
            """
                Args:
                    index (int): Current index in the string being processed.
                    left_rem (int): Remaining number of opening brackets '(' to remove.
                    right_rem (int): Remaining number of closing brackets ')' to remove.
                    open_count (int): Current balance of open brackets (must stay >= 0).
                    current_path (list[str]): List of characters built for the current sequence.

                Returns:
                    None

                Purpose:
                    Recursively traverses the string to determine whether each character should be 
                    kept or removed. Ensures the removed characters match the required count and type 
                    so that all remaining opening brackets have a corresponding closing bracket.
            """
            # Pruning: invalid parentheses sequence
            if open_count < 0 or left_rem < 0 or right_rem < 0:
                return

            # Base case: processed entire string
            if index == len(s):
                if left_rem == 0 and right_rem == 0 and open_count == 0:
                    result.add("".join(current_path))
                return

            char = s[index]

            # Option 1: Remove current bracket
            if char == '(' and left_rem > 0:
                backtrack(index + 1, left_rem - 1, right_rem, open_count, current_path)
            elif char == ')' and right_rem > 0:
                backtrack(index + 1, left_rem, right_rem - 1, open_count, current_path)

            # Option 2: Keep current character
            current_path.append(char)
            if char == '(': # if its an open bracket, you need an additional closing bracket
                backtrack(index + 1, left_rem, right_rem, open_count + 1, current_path)
            elif char == ')': # if it is a cose bracket, it should match with an open bracket (else this will be removed in the next pass)
                backtrack(index + 1, left_rem, right_rem, open_count - 1, current_path)
            else: # for all other characters, continue
                backtrack(index + 1, left_rem, right_rem, open_count, current_path)
            
            current_path.pop()  # Backtrack step

        backtrack(0, left_rem, right_rem, 0, [])
        return list(result)


'''
    Using a combination of gemini.ai and the Edutorial, i was able to generate this funcitonal code.
    I am yet to understand how i wokrs, but due to time constraints, I will leave my understanding
    and worked decription until tomorrow.
'''
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Step 1: Calculate exact counts of misplaced opening and closing brackets
        left_rem = 0
        right_rem = 0
        for char in s:
            if char == '(':
                left_rem += 1
            elif char == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        self.ans = set()

        # Step 2: Limited Backtracking
        def dfs(index, left_rem, right_rem, open_count, current_path):
            # Base Case
            if index == len(s):
                if left_rem == 0 and right_rem == 0 and open_count == 0:
                    self.ans.add("".join(current_path))
                return

            char = s[index]

            # Letters are always kept
            if char != '(' and char != ')':
                current_path.append(char)
                dfs(index + 1, left_rem, right_rem, open_count, current_path)
                current_path.pop()
                return

            # Branch 1: Try removing the bracket
            if char == '(' and left_rem > 0:
                dfs(index + 1, left_rem - 1, right_rem, open_count, current_path)
            elif char == ')' and right_rem > 0:
                dfs(index + 1, left_rem, right_rem - 1, open_count, current_path)

            # Branch 2: Try keeping the bracket
            if char == '(':
                current_path.append(char)
                dfs(index + 1, left_rem, right_rem, open_count + 1, current_path)
                current_path.pop()
            elif char == ')' and open_count > 0:  # Only keep ')' if an unmatched '(' exists
                current_path.append(char)
                dfs(index + 1, left_rem, right_rem, open_count - 1, current_path)
                current_path.pop()

        dfs(0, left_rem, right_rem, 0, [])
        return list(self.ans)