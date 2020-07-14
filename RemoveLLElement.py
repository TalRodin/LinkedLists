class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head, val):
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        n_arr=[]
        for i in arr:
            if i!=val:
                n_arr.append(i)
        point=head=ListNode(0)
        for v in n_arr:
            point.next=ListNode(v)
            point=point.next
        return head.next
    def printList(self,head):
            arr=[]
            while head:
                arr.append(str(head.val))
                head=head.next
            return '->'.join(arr)
L1=ListNode(1)
L2=ListNode(2)
L3=ListNode(6)
L4=ListNode(3)
L5=ListNode(4)
L6=ListNode(5)
L7=ListNode(6)
L1.next=L2
L2.next=L3
L3.next=L4
L4.next=L5
L5.next=L6
L6.next=L7
s=Solution()
val=6
print(s.printList(L1))

print(s.printList(s.removeElements(L1,val)))