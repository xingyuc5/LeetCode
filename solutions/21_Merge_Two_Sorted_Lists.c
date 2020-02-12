

struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *resultList, *curr;

    if (l1 == NULL) {
        resultList = l2;
        return resultList;
    }
    if (l2 == NULL) {
        resultList = l1;
        return resultList;
    }

    if (l1->val < l2->val) {
        resultList = l1;
        l1 = l1->next;
    } else {
        resultList = l2;
        l2 = l2->next;
    }
    curr = resultList;

    while (l1 && l2) {
        if (l1->val < l2->val) {
            curr->next = l1;
            curr = curr->next;
            l1 = l1->next;
        } else {
            curr->next = l2;
            curr = curr->next;
            l2 = l2->next;
        }
    }

    if (l1) {
        curr->next = l1;
    } else {
        curr->next = l2;
    }

    return resultList;
}
