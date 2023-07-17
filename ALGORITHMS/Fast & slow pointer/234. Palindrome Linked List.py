# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return 1
        start = fast = slow = head
        while fast and fast.next!= None:
            fast = fast.next.next
            slow = slow.next
        
        end = self.reverse_list(slow)

        while start and end:
            if start.val != end.val:
                return 0
            start = start.next
            end = end.next
        return 1
        
    def reverse_list(self, curr):
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev