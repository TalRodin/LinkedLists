class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        arr1=[]
        arr2=[]
        while l1:
            arr1.append(l1.val)
            l1=l1.next
        while l2:
            arr2.append(l2.val)
            l2=l2.next
        arr=sorted(arr1+arr2)
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
L2=ListNode(2)
L3=ListNode(4)
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

print(s.printList(s.mergeTwoLists(L1,LL1)))