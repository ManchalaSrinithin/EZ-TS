class node:
    def _init_(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class dll:
    def _init_(self):
        self.head = None
        self.tail = None

    def insertatbeg(self, data):
        if self.head is None:
            new_node = node(data)
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            new_node = node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.tail.next = self.head
            self.head.prev = self.tail

    def printx(self):
        if self.head is not None:
            current = self.head
            while True:
                print(current.val, end=" -> ")
                current = current.next
                if current == self.head:
                    break
        print()

    def insertatend(self, data):
        if self.head is None:
            new_node = node(data)
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            new_node = node(data)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail

    def delatend(self):
        if self.head is None:
            return None
        elif self.head.next == self.head:
            valx = self.head.val
            self.head = None
            self.tail = None
            return valx
        else:
            valx = self.tail.val
            self.tail = self.tail.prev
            self.tail.next = self.head
            return valx

    def delatbeg(self):
        if self.head is None:
            return None
        elif self.head.next == self.head:
            valx = self.head.val
            self.head = None
            self.tail = None
            return valx
        else:
            valx = self.head.val
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
            return valx

l = [2, 4, 6, 8, 9]
o = dll()
for i in l:
    o.insertatbeg(i)

o.printx()

o.insertatend(10)
o.printx()

o.delatbeg()
o.printx()

o.delatend()
o.printx()