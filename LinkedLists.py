class ListNode: 
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def __init__(self):
    self.head=None
  def insert_at_beginning(self,data):
    new_node=ListNode(data)
    new_node.next=self.head
    self.head=new_node
  def insert_at_end(self,data):
    new_node=ListNode(data)
    if self.head is None:
      self.head=new_node
      return
    n=self.head
    while n.next:
      n=n.next
    n.next=new_node
  def insert_after_x(self,x,data):
    n=self.head
    while n:
      if n.val==x:
        break
      n=n.next
    new_node=ListNode(data)
    new_node.next=n.next
    n.next=new_node
  def insert_before_x(self,x,data):
    n=self.head
    while n:
      if n.next.val==x:
        break
      n=n.next
    new_node=ListNode(data)
    new_node.next=n.next
    n.next=new_node
  def insert_at_index(self,i,data):
    count=0
    n=self.head
    while count<i-1:
      count+=1
      n=n.next
    new_node=ListNode(data)
    new_node.next=n.next
    n.next=new_node
  






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
  def remove_at_start(self):
      self.head=self.head.next
  def remove_at_end(self):
      n=self.head
      while n.next.next:
        n=n.next
      n.next=None




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
  def create_LL(self):
    nums=int(input('Number: '))
    for i in range(nums):
      val=int(input('Enter value: '))
      self.insert_at_end(val)
    








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

m=Solution()
arr=[1,2,3,4,5]
for i in arr:
  m.insert_at_beginning(i)
print(m.printList(m.head))


for i in arr:
  m.insert_at_end(i)
print(m.printList(m.head))

x=4
m.insert_after_x( x,6)
print(m.printList(m.head))

x=6
m.insert_before_x(x,7)
print(m.printList(m.head))


i=5
m.insert_at_index(i,8)
print(m.printList(m.head))


new_list=Solution()
new_list.create_LL()
print(new_list.printList(new_list.head))
new_list.remove_at_start()
print(new_list.printList(new_list.head))
new_list.remove_at_end()
print(new_list.printList(new_list.head))