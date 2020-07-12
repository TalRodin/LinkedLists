class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        arr=[]
        for l in lists:
            while l:
                arr.append(l.val)
                l=l.next
        arr=sorted(arr)
        point=head=ListNode(0)
        for i in arr:
            point.next=ListNode(i)
            point=point.next
        return head.next

    def printList(self,head):
        arr=[]
        while head:
            arr.append(str(head.val))
            head=head.next
        return '->'.join(arr)
    


L1=ListNode(1)
L2=ListNode(4)
L3=ListNode(5)
L1.next=L2
L2.next=L3
s=Solution()
print(s.printList(L1))
LL1=ListNode(1)
LL2=ListNode(3)
LL3=ListNode(4)
LL1.next=LL2
LL2.next=LL3
s=Solution()
print(s.printList(LL1))
LLL1=ListNode(2)
LLL2=ListNode(6)

LLL1.next=LLL2

s=Solution()
print(s.printList(LLL1))

arr=[L1,LL1,LLL1]
print(arr)
print(s.printList(s.mergeKLists(arr)))