from _heapq import heappush
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return None
        # return self.using_merge(lists)
        return self.using_heap(lists)
    

    # time - O(N log k), space - O(k)
    def using_heap(self, lists):
        heap = []
        for node in lists:
            if not node: continue
            heapq.heappush(heap, (node.val, id(node), node))
        
        dummy = ListNode(0)
        cur = dummy

        while heap:
            node = heapq.heappop(heap)
            cur.next = node[2]
            cur = cur.next
            if (node[2].next): 
                heapq.heappush(heap, (node[2].next.val, id(node[2].next), node[2].next))
        
        return dummy.next


        
    # time - O(N log k), space - O(k) 
    def using_merge(self, lists):
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
