/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

#define node struct ListNode

bool hasCycle(struct ListNode *head) {
    if (head == NULL) {
        return false;
    }

    if (head->next == NULL) {
        return false;
    }

    node *slow = head;
    node *fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            return true;
        }
    }
    return false;
}