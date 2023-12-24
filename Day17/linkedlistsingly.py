class node:
    def __init__(self,val):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            temp=node(data)
            temp.next=self.head
            self.head=temp
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=node(data)
    def deletionatbeg(self):
        if self.head==None:
            return None
        else:
            temp=self.head
            self.head=temp.next
            return temp.next.next.val
    def deletionatend(self):
        if self.head==None:
            return None
        temp=self.head
        while temp.next.next!=None:
            temp=temp.next
        cur=temp.next.val
        temp.next=None
        return cur1
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.val,end=' -> ')
            temp=temp.next

l=list(map(int,input().split()))
o=sll()
for i in l:
    o.insertatend(i)
print(o.deletionatend())
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
