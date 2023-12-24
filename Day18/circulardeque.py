class MyCircularDeque:
    def __init__(self, k: int):
        self.k=k
        self.deque=[]
    def insertFront(self, value: int) -> bool:
        if len(self.deque)<self.k:
            self.deque=[value]+self.deque
            return True
        return False
    def insertLast(self, value: int) -> bool:
        if len(self.deque)<self.k:
            self.deque.append(value)
            return True
        return False
    def deleteFront(self) -> bool:
        if len(self.deque)>0:
            self.deque.pop(0)
            return True
        return False
    def deleteLast(self) -> bool:
        if len(self.deque)>0:
            self.deque.pop()
            return True
        return False
    def getFront(self) -> int:
        if len(self.deque)>0:
            Front=self.deque[0]
            return Front
        return -1
    def getRear(self) -> int:
        if len(self.deque)>0:
            Rear=self.deque[-1]
            return Rear
        return -1
    def isEmpty(self) -> bool:
        if len(self.deque)==0:
            return True
    def isFull(self) -> bool:
        if len(self.deque)==self.k:
            return True
obj = MyCircularDeque(k)
 param_1 = obj.insertFront(value)
 param_2 = obj.insertLast(value)
 param_3 = obj.deleteFront()
 param_4 = obj.deleteLast()
 param_5 = obj.getFront()
 param_6 = obj.getRear()
 param_7 = obj.isEmpty()
 param_8 = obj.isFull()
        