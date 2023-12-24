class node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            temp=node(data)
            temp.next=self.head
            self.head.prev=temp
            self.head=temp
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            temp=node(data)
            temp.prev=self.tail
            self.tail.next=temp
            self.tail=temp
    def deletionatbeg(self):
        if self.head==None:
            return None
        else:
            self.head=self.head.next
            self.head.prev=None
    def deletionatend(self):
        if self.head==None:
            return None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.val,end=' -> ')
            temp=temp.next
    def reverse(self):
        curr=self.head
        while curr:
            curr.prev,curr.next=curr.next,curr.prev
            curr=curr.prev
        self.head,self.tail=self.tail,self.head

l=list(map(int,input().split()))
o=dll()
for i in l:
    o.insertatend(i)
#o.deletionatend()
o.reverse()
o.display()
'''o2=node(2)
o3=node(3)
o1.next=o2
o2.next=o3
print(o1.val,o2.val,o3.val,sep='->')
print(o1.next.val,o2.next.val,o3.next,sep='->')
#or
o1.next=node(2)
o1.next.next=node(3)
print(o1.val,o1.next.val,o1.next.next.val)
head=node(l[0])'''

