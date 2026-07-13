# 2130. Maximum Twin Sum of a Linked List

# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

# Example 1:
# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6. 

# Example 2:
# Input: head = [4,2,2,3]
# Output: 7
# Explanation:
# The nodes with twins present in this linked list are:
# - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
# - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
# Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 

# Example 3:
# Input: head = [1,100000]
# Output: 100001
# Explanation:
# There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

# Constraints:
# The number of nodes in the list is an even integer in the range [2, 105].
# 1 <= Node.val <= 105




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # use 2 pointers (one at the start, one half-way thorugh (but on the reversed list))
        # move each forward and determine the difference
        if not head:
            return 0
            
        # Find the middle - slow will be at the middle when fast is at the end
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse the second half of the linked list
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # 'prev' is now the head of the reversed second half
        
        # Iterate from both ends to find the maximum twin sum
        max_sum = 0
        first_half = head
        second_half = prev
        
        while second_half:  # The second half will finish first or at the same time
            current_sum = first_half.val + second_half.val
            if current_sum > max_sum:
                max_sum = current_sum
                
            first_half = first_half.next
            second_half = second_half.next
            
        return max_sum