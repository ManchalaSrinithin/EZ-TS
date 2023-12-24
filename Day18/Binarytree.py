class node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    def printing(self):
        if self is None:
            return
        if self.left is not None:
            self.left.printing()
        print(self.data)
        if self.right is not None:
            self.right.printing()
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.printing()
