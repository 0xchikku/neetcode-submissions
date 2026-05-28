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
     * @param {ListNode} head
     * @return {void}
     */
    // time - O(n), space - O(1)
    reorderList(head) {

        // find middle of the list and split
        let slow = head;
        let fast = head;
        while (fast.next && fast.next.next) {
            slow = slow.next;
            fast = fast.next.next;
        }
        const middle = slow.next;
        slow.next = null;

        // reverse the list from middle to tail
        let prev = null;
        let cur = middle;
        while (cur) {
            const next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        const reversedList = prev;

        // merge both the list
        let l1 = head;
        let l2 = reversedList;
        while (l2) {
            const l1Next = l1.next;
            const l2Next = l2.next;
            l1.next = l2;
            l2.next = l1Next;
            l1 = l1Next;
            l2 = l2Next;
        }
    }
}
