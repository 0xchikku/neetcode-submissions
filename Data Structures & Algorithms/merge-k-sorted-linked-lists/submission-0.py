# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    # time - O(N log k), space - O(k) 
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        while len(lists) > 1:
            new_list = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                new_list.append(self.mergeLists(list1, list2))
            lists = new_list
        return lists[0]
    
    # time - O(n+m), space - O(1)
    def mergeLists(self, list1, list2):
        if not list1: return list2
        if not list2: return list1
        dummy = ListNode(0)
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next
