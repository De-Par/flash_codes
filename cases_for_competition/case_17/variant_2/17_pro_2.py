def isPal(x):
    s = str(x); f = True
    for i in range((len(s)+1)//2):
        if s[i] != s[len(s)-i-1]:
            f = False
            break
    return f

p = [int(x) for x in open('17_file_2.txt')]; l = []
count = 0
mx18 = max(x for x in p if isPal(x) and x%18==0)

for a,b,c in zip(p, p[1:], p[2:]):
    if (b-a) == (c-b) and (int(a<mx18)+int(b<mx18)+int(c<mx18)) == 2:
        count += 1
        l += [a+b+c]
l.sort()
if len(l)%2==0:
    print(count, (l[len(l)//2]+l[len(l)//2-1])/2)
else:
    print(count, l[len(l)//2])
