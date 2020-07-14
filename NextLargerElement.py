class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head):
  
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        new_arr=[]
  
        for i in range(len(arr)):

            for n in arr[i+1:]:
                if arr[i]<n:
                    new_arr.append(n)
                    break
            else:
                new_arr.append(0)
        return new_arr
    def printList(self,head):
            arr=[]
            while head:
                arr.append(str(head.val))
                head=head.next
            return '->'.join(arr)

L1=ListNode(2)
L2=ListNode(1)
L3=ListNode(5)

L1.next=L2
L2.next=L3


s=Solution()
print(s.printList(L1))

print(s.nextLargerNodes(L1))