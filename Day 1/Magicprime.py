class Magicprime:
    def __init__(self, n):
        self.n=n
        self.c=1
        for i in range(2,int(n/2)+1):
            if n%i==0:
                self.c+= 1
    def count(self):
        if self.c==1:
            return 1
        else:
            return 0
class reverse:
    def __init__(self, n):
        self.n=n
        n_str=str(n)
        self.rev_n=int(n_str[::-1])
    def string(self):
        return self.rev_n
class display(Magicprime, reverse):
    def __init__(self, n):
        Magicprime.__init__(self, n)
        reverse.__init__(self, n)
        if self.count()==1:
            Magicprime.__init__(self,self.string())
            if self.count()==1:
                if self.string()==self.n:
                    print("prime Magic number")
                else:
                    print("Not a prime Magic number")
        else:
            print("Not a Magic number")
l = int(input("Enter a number: "))
obj = display(l)
