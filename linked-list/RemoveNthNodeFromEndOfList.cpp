/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        auto dummy = new ListNode(0);
        dummy->next = head;

        auto fast = dummy;
        auto slow = dummy;

        while (n >= 0 && fast != nullptr) {
            fast = fast->next;
            n--;
        }

        while (fast != nullptr) {
            fast = fast->next;
            slow = slow->next;
        }

        auto toRemove = slow->next;
        if (toRemove != nullptr) {
            slow->next = toRemove->next;
        }

        return dummy->next;
    }
};
