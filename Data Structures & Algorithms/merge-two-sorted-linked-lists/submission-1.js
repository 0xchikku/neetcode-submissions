/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        // return this.iterative(list1, list2)
        return this.recursive(list1, list2)
    }

    iterative(list1, list2) {
        const dummy = new ListNode(0)
        let cur = dummy

        while (list1 && list2) {
            if (list1.val < list2.val) {
                cur.next = list1;
                [list1, cur] = [list1.next, cur.next]
            } else {
                cur.next = list2;
                [list2, cur] = [list2.next, cur.next]
            }
        }

        cur.next = list1 || list2
        return dummy.next
    }

    recursive(list1, list2) {
        if (!list1 || !list2) return list1 ? list1 : list2

        if (list1.val < list2.val) {
            list1.next = this.recursive(list1.next, list2)
            return list1
        } else {
            list2.next = this.recursive(list1, list2.next)
            return list2
        }
    }
}
