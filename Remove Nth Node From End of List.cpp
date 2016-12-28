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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *temp1 = head;
        ListNode *temp2 = temp1;
        int l = Length(temp1);
        int a = l-n;
        int b=0;
        if(a==0){
            head = temp1->next;
            temp1 = NULL;
            return head;
        }
        while(temp1!=NULL && b<a){
            temp2 = temp1;
            temp1 = temp1->next;
            b+=1;
        }
        temp2->next = temp1->next;
        temp1 = NULL;
        return head;
        
    }
    
    int Length(ListNode *head){
        ListNode *p = head;
        int l = 0;
        while(p!=NULL){
            p = p->next;
            l+=1;
        }
        return l;
    }
};