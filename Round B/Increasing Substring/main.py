def main(n, s):
    n+=1
    ans = [1]
    for k in range(2, n):
        sub = s[0:k]
        if sub[-1]>sub[-2]:
            ans.append(ans[-1]+1)
        else:
            ans.append(1)
    return ' '.join(str(x) for x in ans)

t = int(input())
for i in range(1,t+1):
    n = int(input())
    s = str(input())
    print("Case #{}: {}".format(i, main(n, s)))
