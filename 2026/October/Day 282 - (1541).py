# 1541. Minimum Insertions to Balance a Parentheses String

# Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:
# Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
# Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
# In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.
# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
# You can insert the characters '(' and ')' at any position of the string to balance it if needed.
# Return the minimum number of insertions needed to make s balanced.

# Example 1:
# Input: s = "(()))"
# Output: 1
# Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to add one more ')' at the end of the string to be "(())))" which is balanced.

# Example 2:
# Input: s = "())"
# Output: 0
# Explanation: The string is already balanced.

# Example 3:
# Input: s = "))())("
# Output: 3
# Explanation: Add '(' to match the first '))', Add '))' to match the last '('.

# Constraints:
# 1 <= s.length <= 105
# s consists of '(' and ')' only.

class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        # apply the same code as before
        # This is about character insertion so dont need to consider deleting cases (Used as a base - Code from Problem: 921)


        insertions = 0
        needed_closing = 0
        
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                # Each '(' needs 2 closing ')'
                needed_closing += 2
                
                # If needed_closing is odd, it means we had an unmatched single ')' 
                # earlier, so we insert a ')' to complete that pair and decrease count.
                if needed_closing % 2 == 1:
                    insertions += 1
                    needed_closing -= 1
            else:
                # We encountered a ')'
                needed_closing -= 1
                
                # If needed_closing dropped below 0, we found a ')' without a matching '('
                # We must insert an opening '(' (which adds 2 to needed_closing, making it 1)
                if needed_closing < 0:
                    insertions += 1
                    needed_closing += 2
                    
            i += 1
            
        return insertions + needed_closing