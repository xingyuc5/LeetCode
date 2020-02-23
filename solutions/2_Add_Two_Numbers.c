/**
 * Definition for singly-linked list.
 *
 **/
struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    // Base case
    if (!l1) {
        return l2;
    }
    if (!l2) {
        return l1;
    }

    // Normal case
    struct ListNode* prev;
    struct ListNode* curr1 = l1;
    struct ListNode* curr2 = l2;
    int carryBit = 0;

    while (curr1 && curr2) {
        prev = curr1;
        // Sum two nodes and carrybit
        int sum = curr1->val + curr2->val + carryBit;

        // If equals or greater than 10, carry forward
        if (sum >= 10) {
            curr1->val = sum - 10;
            carryBit = 1;
        } else {
            curr1->val = sum;
            carryBit = 0;
        }

        // Proceed to next node
        curr1 = curr1->next;
        curr2 = curr2->next;
    }
    struct ListNode* rest;
    // If l1 is shorter than l2
    if (curr2) {
        prev->next = curr2;
        rest = curr2;
    } else if (curr1) {
        rest = curr1;
    }

    // While carrybit is non-0
    while (carryBit && rest) {
        prev = rest;

        // Update node and carryBit
        if (rest->val + carryBit == 10) {
            rest->val = 0;
        } else {
            rest->val += carryBit;
            carryBit = 0;
        }
        rest = rest->next;
    }

    // If the list ends and carry bit is still 1, add a new node
    if (carryBit) {
        struct ListNode* newNode = malloc(sizeof(struct ListNode));
        newNode->val = 1;
        newNode->next = NULL;
        prev->next = newNode;
    }

    return l1;
}