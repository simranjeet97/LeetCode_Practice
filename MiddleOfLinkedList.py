class Solution(object):
    def middleNode(self, head):
        if head is None:
            return
        slow,fast = head,head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
