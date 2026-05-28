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
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    // Time - O(max(n, m)), Space - O(max(n, m))
    addTwoNumbers(l1, l2) {
        const dummy = new ListNode(0)
        let cur = dummy
        let carry = 0
        while (l1 || l2 || carry) {
            const sum = (l1?.val ?? 0) + (l2?.val ?? 0) + carry
            const digit = sum % 10
            carry = Math.floor(sum / 10)
            cur.next = new ListNode(digit)
            cur = cur.next
            l1 = l1?.next
            l2 = l2?.next
        }
        return dummy.next
    }
}
