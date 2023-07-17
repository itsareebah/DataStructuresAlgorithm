# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        start = fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        end = self.reverse_list(slow)

        while end and head:
            temp = head.next
            head.next = end
            head = head.next
            head.next = temp
            end = end.next

    def reverse_list(self, curr):
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev