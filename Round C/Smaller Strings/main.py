class small:
    def __init__(self, s, n, k):
        self.s = s
        self.n = n
        self.k = k
        self.answer = []
    def isPalindrome(self, string):
        if string==string[::-1]:
            return True
        return False
    def getStrings(self, set, prefix, k, n):
        if k==0:
            if self.isPalindrome(prefix) and prefix<self.s:
                self.answer.append(prefix)
            else:
                pass
        else:
            for i in range(n):
                newprefix = prefix+set[i]
                self.getStrings(set, newprefix, k-1, n)

    def main(self):
        lis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.getStrings(lis[0:self.k], "", self.n, self.k)
        return len(self.answer)



t = int(input())
for i in range(1,t+1):
    n,k = map(int, input().split())
    s = str(input())
    a = small(s, n, k)
    print("Case #{}: {}".format(i, a.main()))
