p = [int(x) for x in open('17_file_0.txt')]
count = 0; mx = float('-inf')
for a,b,c in zip(p, p[1:], p[2:]):
    mx_n = max(a,b,c)
    if mx_n**2 == (a+b+c-mx_n)**2 - 2*a*b*c/mx_n:
        count += 1
        mx = max(mx, a*b*c*0.5/mx_n)
print(count, mx)

# 7 221130.0
