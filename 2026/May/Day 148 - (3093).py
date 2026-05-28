# 3093. Longest Common Suffix Queries

# You are given two arrays of strings wordsContainer and wordsQuery.
# For each wordsQuery[i], you need to find a string from wordsContainer that has the longest common suffix with wordsQuery[i]. If there are two or more strings in wordsContainer that share the longest common suffix, find the string that is the smallest in length. If there are two or more such strings that have the same smallest length, find the one that occurred earlier in wordsContainer.
# Return an array of integers ans, where ans[i] is the index of the string in wordsContainer that has the longest common suffix with wordsQuery[i].

# Example 1:
# Input: wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]
# Output: [1,1,1]
# Explanation:
# Let's look at each wordsQuery[i] separately:
# For wordsQuery[0] = "cd", strings from wordsContainer that share the longest common suffix "cd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
# For wordsQuery[1] = "bcd", strings from wordsContainer that share the longest common suffix "bcd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
# For wordsQuery[2] = "xyz", there is no string from wordsContainer that shares a common suffix. Hence the longest common suffix is "", that is shared with strings at index 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.

# Example 2:
# Input: wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]
# Output: [2,0,2]
# Explanation:
# Let's look at each wordsQuery[i] separately:
# For wordsQuery[0] = "gh", strings from wordsContainer that share the longest common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.
# For wordsQuery[1] = "acbfgh", only the string at index 0 shares the longest common suffix "fgh". Hence it is the answer, even though the string at index 2 is shorter.
# For wordsQuery[2] = "acbfegh", strings from wordsContainer that share the longest common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.

# Constraints:
# 1 <= wordsContainer.length, wordsQuery.length <= 104
# 1 <= wordsContainer[i].length <= 5 * 103
# 1 <= wordsQuery[i].length <= 5 * 103
# wordsContainer[i] consists only of lowercase English letters.
# wordsQuery[i] consists only of lowercase English letters.
# Sum of wordsContainer[i].length is at most 5 * 105.
# Sum of wordsQuery[i].length is at most 5 * 105.






class TrieNode:
    def __init__(self, best_index, best_length):
        self.children = {}
        self.best_index = best_index
        self.best_length = best_length

    @staticmethod
    def build_trie(wordsContainer):
        global_best_idx = 0
        min_len = float('inf')
        
        # determine the minimum length word
        for i, word in enumerate(wordsContainer):
            if len(word) < min_len:
                min_len = len(word)
                global_best_idx = i
                
        root = TrieNode(global_best_idx, min_len)
        
        for i, word in enumerate(wordsContainer):
            current_len = len(word)
            #start form the node, move through the tree. stepping with each character
            node = root
            # for every character, form the tree
            for char in reversed(word):
                if char not in node.children: #adding new node
                    node.children[char] = TrieNode(i, current_len)
                else: #if already in the tree, check if this word is shorter than the current best (shortest prefix)
                    target_node = node.children[char]
                    # Update if current word is strictly shorter
                    if current_len < target_node.best_length:
                        target_node.best_length = current_len
                        target_node.best_index = i
                node = node.children[char]
        return root

    def search(self, word):
        node = self
        # Move down the tree as long as characters match
        for char in reversed(word):
            if char in node.children:
                node = node.children[char]
            else:
                # Mismatch found: return the best index at the last matching node
                break
        return node.best_index


class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """

        # following the hints
        # root is the index of the shortest string (in the event no suffixes match)
        # form a character tree (in reverse order) - so it is then a longest prefix problem
        trie_root = TrieNode.build_trie(wordsContainer)

        res = []
        # loop through every word in the wordsQuery, going through the trie
        #   when you hit the end of a word or a mismatch character, return the last correct node
        for word in wordsQuery:
            res.append(trie_root.search(word))
        
        return res
    

'''
Made use of gemini.ai to understand the problem and then hints to form the code. I wouldnt have thought of the problem in this way without the help.
However, upon completion, it makes much more sense and seems trivial in highnsight.
Overall principle:
-   form a tree formed by moving with each character backwards in words (this turns it into a longest prefix problem)
-   assign a min length to each
        for each location, check if the new word makes a smaller answer (this word is smaller than another with the same suffix), if so, change the value to match this
-   then go through with each word in the other list, return the last valid point for that word after following through the tree
'''