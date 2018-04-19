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
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == NULL){
            return NULL;
        }
        ListNode *tail = head;
        int listlength = 1;
        while(tail->next){              //����������
            tail = tail->next;
            listlength++;
        }
        k = k % listlength;             //k���ܴ�������ĳ���
        if(k == 0){                     //k����������,����ת
            return head;
        }
        k = listlength - k;             //�ƶ�ǰ��listlength-k���ڵ㵽�Ҳ�,��k���ڵ㲻��
        tail->next = head;              //β�ڵ������׽ڵ�
        ListNode *newlist = head;
        for(int index = 0; index < k-1; index++){      //�Ҷ�������ͷ
            newlist = newlist->next;
        }
        head = newlist->next;           //������ͷ
        newlist->next = NULL;           //�����β��ֵNULL
        return head;                    //��������ͷ���
    }
};