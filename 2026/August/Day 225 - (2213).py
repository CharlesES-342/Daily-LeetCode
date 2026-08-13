# 2213. Longest Substring of One Repeating Character

# You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.
# The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].
# Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.

# Example 1:
# Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
# Output: [3,3,4]
# Explanation: 
# - 1st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
# - 2nd query updates s = "bbbccc". 
#   The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
# - 3rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
# Thus, we return [3,3,4].

# Example 2:
# Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
# Output: [2,3]
# Explanation:
# - 1st query updates s = "abazz". The longest substring consisting of one repeating character is "zz" with length 2.
# - 2nd query updates s = "aaazz". The longest substring consisting of one repeating character is "aaa" with length 3.
# Thus, we return [2,3].

# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.
# k == queryCharacters.length == queryIndices.length
# 1 <= k <= 105
# queryCharacters consists of lowercase English letters.
# 0 <= queryIndices[i] < s.length

'''
Using Gemini.ai, this was the first attempt at the solution. Using this stratagy it would acheive O(n) for
tree population and then O(log n) for each query/modificaiton.
'''
class SegmentTreeNode:
    def __init__(self):
        self.left_char = ''
        self.right_char = ''
        self.prefix_len = 0
        self.suffix_len = 0
        self.max_len = 0
        self.total_len = 0

class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s)
        s_list = list(s)
        tree = [SegmentTreeNode() for _ in range(4 * n)]
        
        def merge(left_node, right_node):
            res = SegmentTreeNode()
            res.total_len = left_node.total_len + right_node.total_len #combine lengths of each child
            res.left_char = left_node.left_char #take new left character
            res.right_char = right_node.right_char #take new right character

            # Determine the new Prefix and Suffuxes

            res.prefix_len = left_node.prefix_len #get the new prefix
            if left_node.prefix_len == left_node.total_len and left_node.right_char == right_node.left_char: #if the prefix is all of the left and some of the right (add both these sections together to make one larder prefix)
                res.prefix_len += right_node.prefix_len
                
            res.suffix_len = right_node.suffix_len
            if right_node.suffix_len == right_node.total_len and right_node.right_char == left_node.right_char: #if the suffix is all of the right and some of the left (add both these sections together to make one larger suffix)
                res.suffix_len += left_node.suffix_len
                
            # New max array of contiunuous characters: can be from each side, or stretch over both sides
            res.max_len = max(left_node.max_len, right_node.max_len)
            if left_node.right_char == right_node.left_char:
                res.max_len = max(res.max_len, left_node.suffix_len + right_node.prefix_len)
                
            return res

        def build(node, start, end):
            '''
            Form a base empty tree
            Then populate with the initial array
            '''
            if start == end:
                tree[node].left_char = s_list[start]
                tree[node].right_char = s_list[start]
                tree[node].prefix_len = 1
                tree[node].suffix_len = 1
                tree[node].max_len = 1
                tree[node].total_len = 1
                return
            
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def update(node, start, end, idx, char):
            '''
            For processing the queries and adding new characters
            Go down the apropriate branch of the tree to add the character to update the tree (this causes the re-calculation of prefix and suffix lengths for that leaf, which follows back up the tree)
            '''
            if start == end:
                s_list[idx] = char
                tree[node].left_char = char
                tree[node].right_char = char
                return
            
            mid = (start + end) // 2
            # recursivelly effect up the tree
            if start <= idx <= mid:
                update(2 * node, start, mid, idx, char)
            else:
                update(2 * node + 1, mid + 1, end, idx, char)
            
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        build(1, 0, n - 1)
        
        ans = []
        # group modifications and queries together to ensure they remain in sync
        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char) # perform the update
            ans.append(tree[1].max_len) # determine the new max character length following this (this is always thje length at the max length at the top of the tree)
            
        return ans

'''
However, this was ineficient, only competing 56/57 of the test cases in time.
This is likely due to the use of additional data structures which increase the time complexity.
Instead, it can be beneficiual to use a flatterned tree structure to reduce delay.
'''
class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s)
        s_list = list(s)
        
        # Flatten segment tree arrays for performance
        left_char = [''] * (4 * n)
        right_char = [''] * (4 * n)
        prefix_len = [0] * (4 * n)
        suffix_len = [0] * (4 * n)
        max_len = [0] * (4 * n)
        total_len = [0] * (4 * n)
        
        def push_up(node):
            left_node = 2 * node
            right_node = 2 * node + 1
            
            total_len[node] = total_len[left_node] + total_len[right_node]
            left_char[node] = left_char[left_node]
            right_char[node] = right_char[right_node]
            
            # Prefix length
            prefix_len[node] = prefix_len[left_node]
            if prefix_len[left_node] == total_len[left_node] and right_char[left_node] == left_char[right_node]:
                prefix_len[node] += prefix_len[right_node]
                
            # Suffix length
            suffix_len[node] = suffix_len[right_node]
            if suffix_len[right_node] == total_len[right_node] and right_char[left_node] == left_char[right_node]:
                suffix_len[node] += suffix_len[left_node]
                
            # Max length
            max_len[node] = max(max_len[left_node], max_len[right_node])
            if right_char[left_node] == left_char[right_node]:
                max_len[node] = max(max_len[node], suffix_len[left_node] + prefix_len[right_node])

        def build(node, start, end):
            if start == end:
                c = s_list[start]
                left_char[node] = c
                right_char[node] = c
                prefix_len[node] = 1
                suffix_len[node] = 1
                max_len[node] = 1
                total_len[node] = 1
                return
            
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            push_up(node)

        def update(node, start, end, idx, char):
            if start == end:
                s_list[idx] = char
                left_char[node] = char
                right_char[node] = char
                return
            
            mid = (start + end) // 2
            if start <= idx <= mid:
                update(2 * node, start, mid, idx, char)
            else:
                update(2 * node + 1, mid + 1, end, idx, char)
            
            push_up(node)

        build(1, 0, n - 1)
        
        ans = []
        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            ans.append(max_len[1])
            
        return ans

'''
Whiole I did cheat to get this answer, I do understand the process. However, I do not beleive that I would
have been able to have completed this as efficiently without assistance.
This is one of those that I beleive is slightly above my skill level (without a data structures cheat sheet to
help me set out the segmentation tree structure becuase I simply dont rememeber - a google search would be fine)

In my head I was thinking about breaking it down into character groups and keeping a count of that and then
adding to a group as edge characters are changed and taking away from others (sometimes splitting groups).
However, as I sat back in my chair, I realised that is literally the segmentation data structure, and I was
daft to think that for this problem there was another approach that could acheive this level of effficiency.
'''