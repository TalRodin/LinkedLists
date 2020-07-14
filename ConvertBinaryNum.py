class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head):
        answer=0
        while head:
            answer=2*answer+head.val
            head=head.next
        return answer
    def printList(self,head):
            arr=[]
            while head:
                arr.append(str(head.val))
                head=head.next
            return '->'.join(arr)

L1=ListNode(1)
L2=ListNode(0)
L3=ListNode(1)
L1.next=L2
L2.next=L3
s=Solution()
print(s.printList(L1))

print(s.getDecimalValue(L1))