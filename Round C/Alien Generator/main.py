class kickstart:
    def __init__(self, g):
        self.g = g
        self.ans = 0
    def k_exists(self, i):
        var = self.g - i*(i-1)//2
        if var % i==0:
            return True
        return False
    def main(self):
        i_max = (1+int((1+8*self.g)**0.5))//2 
        for i in range(1,i_max):
            if self.k_exists(i):
                self.ans+=1
        return self.ans

for i in range(1,int(input())+1):
    a = kickstart(int(input()))
    print("Case #{}: {}".format(i,a.main()))
