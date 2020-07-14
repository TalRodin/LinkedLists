class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        n=''
        while head:
            n+=str(head.val)
            head=head.next
        num=str(int(n)+1)
        point=head=ListNode(0)
        for x in num:
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
L2=ListNode(2)
L3=ListNode(3)
L1.next=L2
L2.next=L3
s=Solution()
print(s.printList(L1))

print(s.printList(s.plusOne(L1)))