# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # time - O(n), space - O(1)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        group_start = None
        group_end = None
        group_prev = None
        group_next = None
        reverse_group_head = None
        dummy = ListNode(0, head)
        cur = dummy

        while True:
            group_prev = cur
            group_start = cur.next
            kth_node = self.find_kth_node(cur, k)
            if not kth_node: 
                break
            group_end = kth_node
            group_next = group_end.next
            group_end.next = None
            reverse_group_head = self.reverse_group(group_start)
            group_prev.next = reverse_group_head
            group_start.next = group_next
            cur = group_start
        
        return dummy.next
    
    def reverse_group(self, head):
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
    
    def find_kth_node(self, cur, k):
        for _ in range(k):
            if not cur: 
                return None
            cur = cur.next
        return cur