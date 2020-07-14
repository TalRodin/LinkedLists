class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        arr=sorted(arr)
        point=head=ListNode(0)
        for x in arr:
            point.next=ListNode(x)
            point=point.next
        return head.next
    def printList(self,head):
            arr=[]
            while head:
                arr.append(str(head.val))
                head=head.next
            return '->'.join(arr)
L1=ListNode(4)
L2=ListNode(2)
L3=ListNode(1)
L4=ListNode(3)
L1.next=L2
L2.next=L3
L3.next=L4

s=Solution()

print(s.printList(L1))


print(s.printList(s.sortList(L1)))
