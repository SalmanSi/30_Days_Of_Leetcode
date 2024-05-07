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
    int carry=0;
    ListNode* doubleIt(ListNode* head) {
         
        if(head!=nullptr)
        {
            head->val=head->val*2;
            doubleIt(head->next);
            head->val+=carry;
            if(head->val>9){
                head->val=head->val-10;
                carry=1;
            }else{
                carry=0;
            }
        }  
        if(carry ==1){
            
            ListNode* new_node= new ListNode;
            new_node->val=1;
            new_node->next=head;
            return new_node;
        }
        return head;

    }
};