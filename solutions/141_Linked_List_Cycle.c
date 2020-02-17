#include <stdbool.h>
#include <stdio.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode* next;
};

bool hasCycle(struct ListNode* head) {
    if (!head || !head->next) {
        return false;
    }

    struct ListNode* slow = head;
    struct ListNode* fast = head;

    while (fast && fast->next) {
        fast = fast->next->next;
        slow = slow->next;

        if (fast == slow) {
            return true;
        }
    }

    return false;
}