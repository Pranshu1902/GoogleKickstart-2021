class kickstart:
    def __init__(self, s, n, k):
        self.s = s
        self.n = n
        self.k = k
    def goodness_score(self):
        score = 0
        for i in range(self.n//2):
            if self.s[i]!=self.s[self.n-i-1]:
                score+=1
        return score
    def answer(self, initial):
        if self.k>initial:
            return self.k-initial
        else:
            return initial-self.k
test_cases = int(input())
for i in range(1,test_cases+1):
    n,k = map(int, input().split())
    s = input()
    run = kickstart(s, n, k)
    ans = run.answer(run.goodness_score())
    print("Case #"+str(i)+": "+str(ans))
