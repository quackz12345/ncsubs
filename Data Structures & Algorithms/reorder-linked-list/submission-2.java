/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        ListNode tail = null, curr = head, p, temp;
        p = curr;
        while(p.next != tail)p = p.next;
        tail = p;
        while(curr.next != null && curr.next.next != null){
            temp = curr.next;
            curr.next = tail;
            curr.next.next = temp;
            curr = curr.next.next;
            p = curr;
            while(p.next != tail)p = p.next;
            p.next = null;
            tail = p;
        }
        

    }
}
