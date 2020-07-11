class ListNode: 
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def __init__(self):
    self.head=None
  def printList(self, node):
      arr=[]    
      while node:
        arr.append(node.val)
        node=node.next
      return arr
  def printRecursion(self, node):
      if node is None:
        return None       
      head = node
      tail = node.next
      self.printRecursion(tail)
      print(head.val)
  def print_backward_nicely(self, list):
      print("[", end=" ")
      self.printRecursion(list)
      print("]")
  def removeNode(self, node):
      head=node
      tail=node.next
      head.next=tail.next
      tail.next=None
      return tail.val
  def count(self,node):
    count=0
    while node:
      count+=1
      node=node.next
    return count
  def search(self,x,node):
    while node:
      if node.val==x:
        return True
      node=node.next
    return False
  def reverseLL(self, head):
    prev=None
    node=head
    while node:
      next=node.next
      node.next=prev
      prev=node
      node=next
    arr=[]
    while prev:
      if prev.next:
        print('val:',prev.val,' next:', prev.next.val)
      else:
        print('val:',prev.val,' next:', None)
      arr.append(prev.val)
      prev=prev.next
    return arr
  def merge(self,l1,l2):
    print(self.printList(l1))
    print(self.printList(l2)) 
    point=head=ListNode(0)
    while l1 and l2:
      if l1.val<=l2.val:
        point.next=ListNode(l1.val)
        l1=l1.next
      else:
        point.next=ListNode(l2.val)
        l2=l2.next
      point=point.next
    if l1 is None:
      point.next=l2
    else:
      point.next=l1
    print(self.printList(head.next)) 
    return head.next
    








node = ListNode("test")
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node.next=node1
node1.next = node2
node2.next = node3
print(node1.next.val)
n=Solution()
print(n.printList(node))
n.printRecursion(node)
n.print_backward_nicely(node)
removed = n.removeNode(node)
print(removed)
print(n.count(node))
print(n.search(5,node))
print(n.reverseLL(node))
list1=ListNode(1)
list2=ListNode(2)
list3=ListNode(4)
list1.next=list2
list2.next=list3
lst1=ListNode(1)
lst2=ListNode(3)
lst3=ListNode(4)
lst1.next=lst2
lst2.next=lst3
s=Solution()
s.merge(list1,lst1)
s.printList(s.merge(list1,lst1))

# node_start=ListNode()
# LL=Solution()
# LL.insert(1,node_start)
# LL.insert(2,node_start)
# LL.insert(3,node_start)
# LL.insert(4,node_start)
# LL.insert(5,node_start)
# print(LL.printList(node_start))