n,m,a,b = raw_input().split()
temp1 = 0
temp2 = 0
temp1 = long(temp1)
temp2 = long(temp2)
n = long(int(n))
m = long(int(m))
a = long(int(a))
b = long(int(b))

if n%m==0:
   print 0
elif n>m:
    temp1 = (n/m+1)*m-n
    temp2 = n%m
    print min(temp1*a,temp2*b)
else:
    temp1 = m-n
    temp2 = n
    print min(temp1*a,temp2*b)
    
   
