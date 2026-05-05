# 61. Rotate List

# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

# Constraints:
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        # change the n-(k+1)th element to point to nothing
        # change the final element to point to the 1st element (if len MOD k != 0)
        # set head to the n-k th element
        
        # Edge case: empty list, single node, or no rotation needed
        if not head or not head.next or k == 0:
            return head

        #find the tail and determine the length
        old_tail = head
        length = 1
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
        
        # join the tail to the head to make it circular
        old_tail.next = head

        k = k % length # simplify the roataion if k >= length
        new_tail_steps = length - k - 1 #new tail location
        
        new_tail = head
        for _ in range(new_tail_steps):
            new_tail = new_tail.next
            
        # set the new head and break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head