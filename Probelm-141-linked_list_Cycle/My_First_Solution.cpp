//My First Sol
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr) return false;
        if (head->next == nullptr) return false;

        unordered_map<ListNode*, bool> mp; 
        ListNode* temp = head;

        while (temp != nullptr) {
            if (mp[temp] == true) {
                return true;
            }
            mp[temp] = true;
            temp = temp->next;
        }

        return false;
    }
};


