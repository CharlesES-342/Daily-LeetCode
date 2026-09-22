# 3525. Find X Value of Array II

# You are given an array of positive integers nums and a positive integer k. You are also given a 2D array queries, where queries[i] = [indexi, valuei, starti, xi].
# You are allowed to perform an operation once on nums, where you can remove any suffix from nums such that nums remains non-empty.
# The x-value of nums for a given x is defined as the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x modulo k.
# For each query in queries you need to determine the x-value of nums for xi after performing the following actions:
# Update nums[indexi] to valuei. Only this step persists for the rest of the queries.
# Remove the prefix nums[0..(starti - 1)] (where nums[0..(-1)] will be used to represent the empty prefix).
# Return an array result of size queries.length where result[i] is the answer for the ith query.
# A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.
# A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.
# Note that the prefix and suffix to be chosen for the operation can be empty.
# Note that x-value has a different definition in this version.

# Example 1:
# Input: nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]
# Output: [2,2,2]
# Explanation:
# For query 0, nums becomes [1, 2, 2, 4, 5], and the empty prefix must be removed. The possible operations are:
# Remove the suffix [2, 4, 5]. nums becomes [1, 2].
# Remove the empty suffix. nums becomes [1, 2, 2, 4, 5] with a product 80, which gives remainder 2 when divided by 3.
# For query 1, nums becomes [1, 2, 2, 3, 5], and the prefix [1, 2, 2] must be removed. The possible operations are:
# Remove the empty suffix. nums becomes [3, 5].
# Remove the suffix [5]. nums becomes [3].
# For query 2, nums becomes [1, 2, 2, 3, 5], and the empty prefix must be removed. The possible operations are:
# Remove the suffix [2, 2, 3, 5]. nums becomes [1].
# Remove the suffix [3, 5]. nums becomes [1, 2, 2].

# Example 2:
# Input: nums = [1,2,4,8,16,32], k = 4, queries = [[0,2,0,2],[0,2,0,1]]
# Output: [1,0]
# Explanation:
# For query 0, nums becomes [2, 2, 4, 8, 16, 32]. The only possible operation is:
# Remove the suffix [2, 4, 8, 16, 32].
# For query 1, nums becomes [2, 2, 4, 8, 16, 32]. There is no possible way to perform the operation.

# Example 3:
# Input: nums = [1,1,2,1,1], k = 2, queries = [[2,1,0,1]]
# Output: [5]

# Constraints:
# 1 <= nums[i] <= 109
# 1 <= nums.length <= 105
# 1 <= k <= 5
# 1 <= queries.length <= 2 * 104
# queries[i] == [indexi, valuei, starti, xi]
# 0 <= indexi <= nums.length - 1
# 1 <= valuei <= 109
# 0 <= starti <= nums.length - 1
# 0 <= xi <= k - 1


class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree = [None] * (4 * self.n)
        self.build(nums, 1, 0, self.n - 1)

    def _create_leaf(self, val):
        '''Each leaf stores the remainder for teh individual element'''
        rem = val % self.k
        freq = [0] * self.k
        freq[rem] = 1
        return {'prod': rem, 'freq': freq}

    def _merge(self, L, R):
        '''Work from the leaves up the tree to form a total tree'''
        # handle empty sub-trees (edge cases)
        if not L: return R
        if not R: return L
        
        #for each level up, add the count of counts of k remainders
        prod = (L['prod'] * R['prod']) % self.k
        freq = list(L['freq'])
        
        for r in range(self.k):
            if R['freq'][r] > 0:
                new_rem = (L['prod'] * r) % self.k
                freq[new_rem] += R['freq'][r]
                
        return {'prod': prod, 'freq': freq}

    def build(self, nums, node, l, r):
        '''construct the tree'''
        if l == r:
            self.tree[node] = self._create_leaf(nums[l])
            return
        mid = (l + r) // 2
        self.build(nums, 2 * node, l, mid)
        self.build(nums, 2 * node + 1, mid + 1, r)
        self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1])

    def update(self, node, l, r, idx, val):
        '''Change values and feed the changes up the tree'''
        if l == r:
            self.tree[node] = self._create_leaf(val)
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)
        self.tree[node] = self._merge(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node, l, r, ql, qr):
        '''process a query'''
        # see if there are enough values to process, if not, return this element alone in the range
        if ql <= l and r <= qr:
            return self.tree[node]
        # if more elements, determine each part of the tree and merge the tree to form this section
        mid = (l + r) // 2
        L, R = None, None
        if ql <= mid:
            L = self.query(2 * node, l, mid, ql, qr)
        if qr > mid:
            R = self.query(2 * node + 1, mid + 1, r, ql, qr)
        return self._merge(L, R)


class Solution(object):
    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        seg = SegmentTree(nums,k)
        res = []

        for idx, val, start, x in queries:
            # update the element
            seg.update(1,0,n-1,idx,val)
            # query the section
            res_node = seg.query(1,0,n-1,start,n-1)
            # get frequency of remainder x
            res.append(res_node['freq'][x])

        return res
        

'''
Despite my understanding and thought process leading to some form of tree (based on how previous problems were solved), I completely
forgot how to form a segment tree. While my initial assumptions (ignoring the values and strictly considerting the modulo of the produxt)
was correct, I was unable to implement the tree structure correctly, as a result Gemini.ai was used to help my implementation.
'''