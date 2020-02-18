struct ListNode* swapPairs(struct ListNode* head){
    
    
    if (head == NULL || head->next == NULL) {
        return head;
    } else {
        struct ListNode* next = head->next;
        head->next=swapPairs(next->next);
        next->next=head;
        return next;
    }
}