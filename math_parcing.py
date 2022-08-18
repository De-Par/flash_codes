s = '-10*100/4-90+78-45*23'
print('BEFORE: ', s)

a_op = '*/'; b_op = '+-'; c_op = '.0123456789'
len_s =  len(s)
p1, p2 = 0, 0

while p2<len_s:
    while p2<len_s and s[p2] not in a_op:
        if s[p2] in b_op:
            p1=p2
        p2+=1

    if p2 >= len(s): break
    n1 = float(s[p1:p2])
    delit = True if s[p2] == '/' else False
    tmp = ''
    
    while (p2+1)<len_s and s[p2+1] in c_op:
        p2+=1
        tmp+=s[p2]
        
    n2 = float(tmp)
    new_n = str(round(n1/n2, 3) if delit else round(n1*n2, 3))
    if '-' not in new_n: new_n = '+'+new_n
    s = s[:p1]+new_n+s[p2+1:]
    print(s)
    
    delta = len_s - len(s)
    len_s = len(s)
    p1-=delta; p2-=delta

res = 0
fr=0; 
for i in range(1, len_s):
    if s[i] in b_op:
        res+= float(s[fr:i])
        fr = i
    if i==len_s-1:
        res+= float(s[fr:i+1])
print('AFTER: ', res)

    
    
    
    
