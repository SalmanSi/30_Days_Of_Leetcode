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

    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    ListNode* start=new ListNode(-999);
    ListNode* list3;
    
    list3=start;
    while(1){
        if(list1==nullptr && list2 == nullptr){
            break;
        }
        
        if(list1==nullptr){
            list3->next=list2;
            list2=list2->next;
            break;
        }

        if (list2 == nullptr){
            list3->next= list1;
            list1=list1->next;
            break;
        }

        // if neither is null, place the smaller value
        if(list1->val<=list2->val){
             list3->next=list1;
            list1=list1->next;
        }else{
             list3->next= list2;
            list2=list2->next;            
        }
        list3=list3->next;

    }
        ListNode* result=start->next;
            delete start;
            return result;
    }
};