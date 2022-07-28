p = [int(x) for x in open('17_file_1.txt')]
c = 0; mx = float('-inf')
mx19 = max(x for x in p if x%19==0)
for a,b in zip(p, p[1:]):
    if (int(a%2)+int(b%2))==1 and (a>mx19 or b>mx19):
        c+=1
        mx=max(mx,a+b)
print(c, mx)

# 17 199837
