class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        ind=len(arr)-n
        a=[]
        for i in range(len(arr)):
            if i!=ind:
                a.append(arr[i])
        point=head=ListNode(0)
        for x in a:
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
L4=ListNode(4)
L5=ListNode(5)
L1.next=L2
L2.next=L3
L3.next=L4
L4.next=L5
s=Solution()
n=2
print(s.printList(L1))


print(s.printList(s.removeNthFromEnd(L1,n)))
