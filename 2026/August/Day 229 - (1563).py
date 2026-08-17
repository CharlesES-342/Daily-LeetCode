# 1563. Stone Game V

# There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.
# In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.
# The game ends when there is only one stone remaining. Alice's score is initially zero.
# Return the maximum score that Alice can obtain.

# Example 1:
# Input: stoneValue = [6,2,3,4,5,5]
# Output: 18
# Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
# In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
# The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.

# Example 2:
# Input: stoneValue = [7,7,7,7,7,7,7]
# Output: 28

# Example 3:
# Input: stoneValue = [4]
# Output: 0

# Constraints:
# 1 <= stoneValue.length <= 500
# 1 <= stoneValue[i] <= 106

'''
This solution only worked for 123/132 of the problems
'''
class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        
        # Precompute prefix sums for O(1) subarray sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        def get_sum(i, j):
            return prefix[j + 1] - prefix[i]

        memo = {}

        def dp(i, j):
            # Base case: single stone leads to no turther score
            if i == j:
                return 0
            
            # Check memory
            if (i, j) in memo:
                return memo[(i, j)]
            
            max_score = 0
            
            # Try every possible split point k
            for k in range(i, j):
                left_sum = get_sum(i, k)
                right_sum = get_sum(k + 1, j)
                
                if left_sum < right_sum:
                    # Bob discards right, Alice keeps left
                    max_score = max(max_score, left_sum + dp(i, k))
                elif left_sum > right_sum:
                    # Bob discards left, Alice keeps right
                    max_score = max(max_score, right_sum + dp(k + 1, j))
                else:
                    # Both are equal, Alice chooses the maximum outcome
                    max_score = max(max_score, left_sum + max(dp(i, k), dp(k + 1, j)))
            
            memo[(i, j)] = max_score
            return max_score

        return dp(0, n - 1)

'''
The above code has Complexity O(n^3) because you iterate over all [i,j] and then over all k wihtin those ranges.

Another iteration utilises memorisation of prefixes to pre-comute differences before memorisation. However this
is stioll too slow, only completing 130/132 problems
'''
class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        
        # Precompute prefix sums for O(1) range sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        def get_sum(i, j):
            return prefix[j + 1] - prefix[i]

        memo = {}

        def dp(i, j):
            if i == j:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            max_score = 0
            total_range_sum = get_sum(i, j)
            
            for k in range(i, j):
                left_sum = get_sum(i, k)
                right_sum = total_range_sum - left_sum  # O(1) calculation
                
                # Pruning step to cut down unnecessary iterations
                if max_score >= left_sum * 2 and left_sum > right_sum:
                    break
                
                if left_sum < right_sum:
                    score = left_sum + dp(i, k)
                    if score > max_score:
                        max_score = score
                elif left_sum > right_sum:
                    score = right_sum + dp(k + 1, j)
                    if score > max_score:
                        max_score = score
                else:
                    score = left_sum + max(dp(i, k), dp(k + 1, j))
                    if score > max_score:
                        max_score = score
                        
            memo[(i, j)] = max_score
            return max_score

        return dp(0, n - 1)
    
'''
The following is in O(n^2). This is because the key optimisation, rendering the pointer i as a standard sliding
poiinter as oposed to a nested loop. This is because the sum-left is always increasing, and the total is always
increasing, allowing it to be determined in O(1).
By pre-computinmg the maximums, allm you need to do is iterate over the sub arrays (given pointer locations
to determine the maximum value).

1. Advance i as far right as possible while the left half sum (suml) remains less than or equal to half of the
current total range sum (total/2)
2. Once the split index i is located, the ranges are split into three scenarios:
    - If the left half sum is less than the right half sum, then the maximum score is
    determined by the left half
    - If the left half sum is greater than the right half sum, then the maximum score is
    determined by the right half
    - If the left half sum is equal to the right half sum, then the maximum score is
    determined by the maximum of the left and right halves.
3. update maxl and maxr

As a result the movment of maxl and max r ()outer loop) has a complexity of O(n^2) but moving i has a fixed
length.

This solution was formed by Gemini.ai and was based on the editorian and my initial thought proces where I iterated
over 'i' rather than a fixed size variable. (That is where I was inefficient)
'''
class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        f = [[0] * n for _ in range(n)]
        maxl = [[0] * n for _ in range(n)]
        maxr = [[0] * n for _ in range(n)]

        for left in range(n - 1, -1, -1):
            maxl[left][left] = maxr[left][left] = stoneValue[left]
            total = stoneValue[left]
            suml = 0
            i = left - 1
            
            for right in range(left + 1, n):
                total += stoneValue[right]
                while i + 1 < right and (suml + stoneValue[i + 1]) * 2 <= total:
                    suml += stoneValue[i + 1]
                    i += 1
                    
                if left <= i:
                    f[left][right] = max(f[left][right], maxl[left][i])
                if i + 1 < right:
                    f[left][right] = max(f[left][right], maxr[i + 2][right])
                if suml * 2 == total:
                    f[left][right] = max(f[left][right], maxr[i + 1][right])
                    
                maxl[left][right] = max(
                    maxl[left][right - 1], total + f[left][right]
                )
                maxr[left][right] = max(
                    maxr[left + 1][right], total + f[left][right]
                )

        return f[0][n - 1]