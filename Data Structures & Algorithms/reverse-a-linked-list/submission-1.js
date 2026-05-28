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
     * @return {ListNode}
     */
    reverseList(head) {
        return this.solution0(head)
        // return solution1(head)
    }


    solution0(head) {
        let prev = null
        let curr = head
         
         while (curr) {
            const next = curr.next;
            curr.next = prev;
            [prev, curr] = [curr, next]
         }

         return prev
    }

    solution1(head) {

    }
}
