/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *slowptr,*fastptr;
        slowptr=head;
        fastptr=head;

        while(slowptr!=nullptr && fastptr!=nullptr){
            slowptr=slowptr->next;
            if(fastptr->next==nullptr){
                break;
            }
            fastptr=fastptr->next->next;
            if(slowptr==fastptr){
                return true;
            }
        }
        return false;

    }
};