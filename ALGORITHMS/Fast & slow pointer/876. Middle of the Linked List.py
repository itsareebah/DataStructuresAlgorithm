# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # SOL - 1
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
        # SOL - 2
        count = 0
        front = rev = head
        while rev.next:
            rev = rev.next
            count += 1
        
        count = count/2 + 1 if (count % 2)==0 else int(count/2) + 1

        while count != 0:
            front = front.next
            count -= 1
        
        return front