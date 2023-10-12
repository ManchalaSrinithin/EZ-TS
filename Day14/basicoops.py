class cse:
    def __init__(self):
        self.k=1
    def fun1(self):
        return self.k
class aiml():
    def fun2(self):
        print("Most of the Topics inherited from cse class")
class cse2(cse,aiml):
    def fun3(self,c):
        cse.__init__(self)
        if self.fun1()==1:
            print("Topics inherited from cse and aiml class")
o=cse2()
o.fun3(4)
o.fun2()