class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        arr=sorted(set(arr))
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

L1=ListNode(1)
L2=ListNode(1)
L3=ListNode(2)
L4=ListNode(3)
L5=ListNode(3)
L1.next=L2
L2.next=L3
L3.next=L4
L4.next=L5


s=Solution()

print(s.printList(L1))

print(s.printList(s.deleteDuplicates(L1)))
