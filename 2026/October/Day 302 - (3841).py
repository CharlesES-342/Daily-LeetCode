# 3841. Palindromic Path Queries in a Tree

# You are given an undirected tree with n nodes labeled 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.
# You are also given a string s of length n consisting of lowercase English letters, where s[i] represents the character assigned to node i.
# You are also given a string array queries, where each queries[i] is either:
# "update ui c": Change the character at node ui to c. Formally, update s[ui] = c.
# "query ui vi": Determine whether the string formed by the characters on the unique path from ui to vi (inclusive) can be rearranged into a palindrome.
# Return a boolean array answer, where answer[j] is true if the jth query of type "query ui vi"​​​​​​​ can be rearranged into a palindrome, and false otherwise.

# Example 1:
# Input: n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]
# Output: [true,false]
# Explanation:
# "query 0 2": Path 0 → 1 → 2 gives "aac", which can be rearranged to form "aca", a palindrome. Thus, answer[0] = true.
# "update 1 b": Update node 1 to 'b', now s = "abc".
# "query 0 2": Path characters are "abc", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
# Thus, answer = [true, false].

# Example 2:
# Input: n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]
# Output: [false,false,true]
# Explanation:
# "query 1 2": Path 1 → 0 → 2 gives "bac", which cannot be rearranged to form a palindrome. Thus, answer[0] = false.
# "update 0 b": Update node 0 to 'b', now s = "bbca".
# "query 2 3": Path 2 → 0 → 3 gives "cba", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
# "update 3 a": Update node 3 to 'a', s = "bbca".
# "query 1 3": Path 1 → 0 → 3 gives "bba", which can be rearranged to form "bab", a palindrome. Thus, answer[2] = true.
# Thus, answer = [false, false, true].

# Constraints:
# 1 <= n == s.length <= 5 * 104
# edges.length == n - 1
# edges[i] = [ui, vi]
# 0 <= ui, vi <= n - 1
# s consists of lowercase English letters.
# The input is generated such that edges represents a valid tree.
# 1 <= queries.length <= 5 * 104​​​​​​​
# queries[i] = "update ui c" or
# queries[i] = "query ui vi"
# 0 <= ui, vi <= n - 1
# c is a lowercase English letter.

class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type s: str
        :type queries: List[str]
        :rtype: List[bool]
        """
        # If somehthing can be a palindrome, there will be atmost 1 odd count in the array, the rest will be even. This will allow the path to be stored as a 26 bit array where 0 = even and 1 = odd, in terms of counts. As you step through the path, add 1 to each to flick between 0 and 1, then just count the 1's at the end
        
        # Form a flatterened tree and then form a segment tree
        #   DFS to find subtree depth and pointers
        #   DFS for node assignemnt
        #   Form Segment Tree (each storing the 26 bit integer)

        # On Update(u,c) -> update the character at that position. O(log n) time
        # On Query(u,v) -> jump between positions in o(log n) and combine the segment bimasks with XOR. This should only have (at most) one count of 1's as this will be the middle number

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        chars = [ord(c) - 97 for c in s]
        LOG = max(1, n.bit_length())

        parent = [0] * n
        depth = [0] * n
        base = [0] * n          # static root->v xor mask from the initial string
        tin = [0] * n
        order = []

        # Iterative DFS (preorder) so subtrees are contiguous ranges
        base[0] = 1 << chars[0]
        stack = [0]
        visited = [False] * n
        visited[0] = True
        while stack:
            u = stack.pop()
            tin[u] = len(order)
            order.append(u)
            for w in adj[u]:
                if not visited[w]:
                    visited[w] = True
                    parent[w] = u
                    depth[w] = depth[u] + 1
                    base[w] = base[u] ^ (1 << chars[w])
                    stack.append(w)

        # Subtree sizes -> tout
        size = [1] * n
        for u in reversed(order):
            if u != 0:
                size[parent[u]] += size[u]
        tout = [tin[u] + size[u] - 1 for u in range(n)]

        # Binary lifting
        up = [parent[:]]
        for j in range(1, LOG):
            prev = up[j - 1]
            up.append([prev[prev[v]] for v in range(n)])

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            for j in range(LOG):
                if (diff >> j) & 1:
                    a = up[j][a]
            if a == b:
                return a
            for j in range(LOG - 1, -1, -1):
                if up[j][a] != up[j][b]:
                    a = up[j][a]
                    b = up[j][b]
            return parent[a]

        # Fenwick tree: range XOR update, point query
        bit = [0] * (n + 2)

        def bit_xor(i, val):
            i += 1
            while i <= n + 1:
                bit[i] ^= val
                i += i & -i

        def bit_query(i):
            i += 1
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        def val(v):
            return base[v] ^ bit_query(tin[v])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = ord(parts[2]) - 97
                old = chars[u]
                if old != c:
                    delta = (1 << old) ^ (1 << c)
                    bit_xor(tin[u], delta)
                    bit_xor(tout[u] + 1, delta)
                    chars[u] = c
            else: # the Querying section
                u, v = int(parts[1]), int(parts[2])
                l = lca(u, v)
                m = val(u) ^ val(v) ^ (1 << chars[l])
                ans.append(m & (m - 1) == 0)
        return ans
        

'''
This was generated by Claude.ai. My initial thought process was to use a segment tree
to store the character count for each node. However, following the review of the HINTS,
a more efficint section was to store the odd or even count for each of the 26 characters
(stored as a binary number) using a 26 bit integer.

Following this, I was made aware that this can be fatteren to make it even more efficient.

While Alot of the thought processes (following hint review) was my own, since I am on holiday,
I couldnt be bothered to do the code typing, so I just get Claude.ai to generate it for me based
on my description (which is given as the large comments section at the top of the code)
'''
