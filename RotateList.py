class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        k=k%len(arr)
        print(arr)
        while k>0:
            arr=[arr[-1]]+arr[:-1]
            k-=1
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
L3=ListNode(3)
L4=ListNode(4)
L5=ListNode(5)
L1.next=L2
L2.next=L3
L3.next=L4
L4.next=L5
s=Solution()
k=2
print(s.printList(L1))


print(s.printList(s.rotateRight(L1,k)))