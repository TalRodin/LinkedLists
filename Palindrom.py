class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        return arr==arr[::-1]
    def printList(self,head):
            arr=[]
            while head:
                arr.append(str(head.val))
                head=head.next
            return '->'.join(arr)

L1=ListNode(1)
L2=ListNode(2)
L3=ListNode(2)
L4=ListNode(1)
L1.next=L2
L2.next=L3
L3.next=L4
s=Solution()
print(s.printList(L1))

print(s.isPalindrome(L1))