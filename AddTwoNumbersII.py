class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        num1=''
        num2=''
        while l1:
            num1+=str(l1.val)
            l1=l1.next
        while l2:
            num2+=str(l2.val)
            l2=l2.next
        total=int(num1)+int(num2)
        point=head=ListNode(0)
        for x in str(total):
            point.next=ListNode(x)
            point=point.next
        return head.next
    def printList(self,head):
        arr=[]
        while head:
            arr.append(str(head.val))
            head=head.next
        return ''.join(arr)
L1=ListNode(7)
L2=ListNode(2)
L3=ListNode(4)
L4=ListNode(3)
L1.next=L2
L2.next=L3
L3.next=L4
s=Solution()
print(s.printList(L1))
LL1=ListNode(5)
LL2=ListNode(6)
LL3=ListNode(4)
LL1.next=LL2
LL2.next=LL3
s=Solution()
print(s.printList(LL1))

print(s.printList(s.addTwoNumbers(L1,LL1)))            