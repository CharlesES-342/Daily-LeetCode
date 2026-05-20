# 2657. Find the Prefix Common Array of Two Arrays

# You are given two 0-indexed integer permutations A and B of length n.
# A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.
# Return the prefix common array of A and B.
# A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

# Example 1:
# Input: A = [1,3,2,4], B = [3,1,2,4]
# Output: [0,2,3,4]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
# At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.

# Example 2:
# Input: A = [2,3,1], B = [3,1,2]
# Output: [0,1,3]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: only 3 is common in A and B, so C[1] = 1.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.

# Constraints:
# 1 <= A.length == B.length == n <= 50
# 1 <= A[i], B[i] <= n
# It is guaranteed that A and B are both a permutation of n integers.

class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        #order doesnt matter
        #value can at most jump by 2 (from index 0 to 1 in the case they are the oposite way around)

        #loop thorugh the shortest array
        # mark indexes as counted (as you add to one array, count on the other if it is common)
        #   use a 'remaining' array of all un,used indexes (removing is costly)
        # count the number of common indexes in the final counter array

        #OR

        n = len(A)
        C = []
        
        # the value of common items in the prefix will only ever increase
        seen_count = [0] * (n + 1)
        common_elements = 0
        
        for i in range(n):
            # Process the element from array A
            seen_count[A[i]] += 1
            if seen_count[A[i]] == 2:
                common_elements += 1
                
            # Process the element from array B
            seen_count[B[i]] += 1
            if seen_count[B[i]] == 2:
                common_elements += 1
                
            C.append(common_elements)
            
        return C