class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        tail=len(arr)%k

        for i in range(0,len(arr)-tail,k):
            print(arr[i:i+k])
            arr[i:i+k]=reversed(arr[i:i+k])
        point=head=ListNode(0)
        for v in arr:
            point.next=ListNode(v)
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
k=3
print(s.printList(L1))


print(s.printList(s.reverseKGroup(L1,k)))