# 3501. Maximize Active Section with Trade II

# You are given a binary string s of length n, where:
# '1' represents an active section.
# '0' represents an inactive section.
# You can perform at most one trade to maximize the number of active sections in s. In a trade, you:
# Convert a contiguous block of '1's that is surrounded by '0's to all '0's.
# Afterward, convert a contiguous block of '0's that is surrounded by '1's to all '1's.
# Additionally, you are given a 2D array queries, where queries[i] = [li, ri] represents a substring s[li...ri].
# For each query, determine the maximum possible number of active sections in s after making the optimal trade on the substring s[li...ri].
# Return an array answer, where answer[i] is the result for queries[i].
# Note
# For each query, treat s[li...ri] as if it is augmented with a '1' at both ends, forming t = '1' + s[li...ri] + '1'. The augmented '1's do not contribute to the final count.
# The queries are independent of each other.

# Example 1:
# Input: s = "01", queries = [[0,1]]
# Output: [1]
# Explanation:
# Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

# Example 2:
# Input: s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]]
# Output: [4,3,1,1]
# Explanation:
# Query [0, 3] → Substring "0100" → Augmented to "101001"
# Choose "0100", convert "0100" → "0000" → "1111".
# The final string without augmentation is "1111". The maximum number of active sections is 4.
# Query [0, 2] → Substring "010" → Augmented to "10101"
# Choose "010", convert "010" → "000" → "111".
# The final string without augmentation is "1110". The maximum number of active sections is 3.
# Query [1, 3] → Substring "100" → Augmented to "11001"
# Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.
# Query [2, 3] → Substring "00" → Augmented to "1001"
# Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 1.

# Example 3:
# Input: s = "1000100", queries = [[1,5],[0,6],[0,4]]
# Output: [6,7,2]
# Explanation:
# Query [1, 5] → Substring "00010" → Augmented to "1000101"
# Choose "00010", convert "00010" → "00000" → "11111".
# The final string without augmentation is "1111110". The maximum number of active sections is 6.
# Query [0, 6] → Substring "1000100" → Augmented to "110001001"
# Choose "000100", convert "000100" → "000000" → "111111".
# The final string without augmentation is "1111111". The maximum number of active sections is 7.
# Query [0, 4] → Substring "10001" → Augmented to "1100011"
# Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 2.

# Example 4:
# Input: s = "01010", queries = [[0,3],[1,4],[1,3]]
# Output: [4,4,2]
# Explanation:
# Query [0, 3] → Substring "0101" → Augmented to "101011"
# Choose "010", convert "010" → "000" → "111".
# The final string without augmentation is "11110". The maximum number of active sections is 4.
# Query [1, 4] → Substring "1010" → Augmented to "110101"
# Choose "010", convert "010" → "000" → "111".
# The final string without augmentation is "01111". The maximum number of active sections is 4.
# Query [1, 3] → Substring "101" → Augmented to "11011"
# Because there is no block of '1's surrounded by '0's, no valid trade is possible. The maximum number of active sections is 2.

# Constraints:
# 1 <= n == s.length <= 105
# 1 <= queries.length <= 105
# s[i] is either '0' or '1'.
# queries[i] = [li, ri]
# 0 <= li <= ri < n

from bisect import bisect_left, bisect_right

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(data, 0, 0, self.n - 1)

    def _build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
            return
        mid = (start + end) // 2
        self._build(data, 2 * node + 1, start, mid)
        self._build(data, 2 * node + 2, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, L, R):
        if L > R:
            return 0
        return self._query(0, 0, self.n - 1, L, R)

    def _query(self, node, start, end, L, R):
        if R < start or end < L:
            return 0
        if L <= start and end <= R:
            return self.tree[node]
        mid = (start + end) // 2
        return max(
            self._query(2 * node + 1, start, mid, L, R),
            self._query(2 * node + 2, mid + 1, end, L, R)
        )

class Solution(object):
    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        cnt = s.count("1")
        
        zeroBlocks = []
        blockLeft = []
        blockRight = []
        
        i = 0
        while i < n:
            start = i
            while i < n and s[i] == s[start]:
                i += 1
            if s[start] == "0":
                zeroBlocks.append(i - start)
                blockLeft.append(start)
                blockRight.append(i - 1)
        
        m = len(zeroBlocks)

        if m < 2:
            return [cnt] * len(queries)

        tmpSum = [zeroBlocks[k] + zeroBlocks[k+1] for k in range(m - 1)]
        seg = SegmentTree(tmpSum)
        ans = []

        for left, right in queries:
            i = bisect_left(blockRight, left)
            j = bisect_right(blockLeft, right) - 1

            if i > m - 1 or j < 0 or i >= j:
                ans.append(cnt)
                continue
            
            firstLen = (blockRight[i] - max(blockLeft[i], left) + 1)
            lastLen = (min(blockRight[j], right) - blockLeft[j] + 1)

            if i + 1 == j:
                bestGain = firstLen + lastLen
                ans.append(cnt + bestGain)
                continue
            
            val1 = firstLen + zeroBlocks[i+1]
            val2 = zeroBlocks[j-1] + lastLen
            val3 = seg.query(i + 1, j - 2)
            bestGain = max(val1, val2, val3)
            ans.append(cnt + bestGain)
        
        return ans


    '''
    I failed this problem. In truth I couldnt figure it out as my approach entailed computing the
    every query and then computing the max active sections for each query. This is a very
    inefficient approach and would not work for large inputs.
    
    I also did not consider the fact that the queries are independent of each other, which means
    that I could have precomputed some information about the string s to answer the queries more
    efficiently. This was a key insight that I had missed, which lead to my failure.

    Using the Editorial, I was able to construct a solution that worked for many cases,
    but for others, it failed. I also forgot to build the segment tree, which is a key part of this.

    Please see the full explanation:
    Here is a brief, structured breakdown of how the code works:

    1. The SegmentTree Class
    - Purpose: Built to answer Range Maximum Queries in logarithmic time (O(log m)).
    - __init__ & _build: Takes an array of numbers (tmpSum) and constructs a binary tree where each parent node stores the max of its child nodes.
    - query & _query: Efficiently retrieves the maximum value within any given subarray range [L, R] without iterating through every element.

    2. The Solution Class (maxActiveSectionsAfterTrade)
    - Preprocessing Zero Blocks: 
    - It scans the string s to find all consecutive blocks of zeros. 
    - It records their lengths (zeroBlocks), starting indices (blockLeft), and ending indices (blockRight).
    - Preparing the Segment Tree:
    - It calculates the sum of every pair of adjacent zero blocks (tmpSum = zeroBlocks[k] + zeroBlocks[k+1]) and passes this array into the SegmentTree.
    - Answering Queries:
    For each query range [left, right]:
    1. Binary Search: Uses bisect to find which zero blocks overlap with the query boundaries left and right.
    2. Boundary Adjustments: Calculates the actual truncated lengths of the first and last blocks falling inside the query range (firstLen and lastLen).
    3. Evaluating Gains (bestGain):
        - Case 2 (Two blocks): Combines the truncated ends directly.
        - Case 3 (Multiple blocks): Compares three choices to find the maximum possible gain:
        - val1: The modified first block plus the adjacent block.
        - val2: The modified last block plus the preceding block.
        - val3: The maximum sum of interior adjacent blocks fetched instantly via the Segment Tree.
    4. Final Answer: Adds the best gain found to the total initial count of ones (cnt) and appends it to the results.
    '''