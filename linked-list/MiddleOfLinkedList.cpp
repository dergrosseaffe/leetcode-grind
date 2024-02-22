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
    ListNode* middleNode(ListNode* head) {
        ListNode* middle = head;
        int i = 0;

        while (head != nullptr) {
            head = head->next;
            i++;

            // moves middle pointer every two head moves ensuring it will be
            // in the middle of the list when head reaches the end
            if (i % 2 == 0) middle = middle->next;
        }

        return middle;
    }
};
