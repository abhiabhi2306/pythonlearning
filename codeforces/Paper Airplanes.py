k,n,s,p = raw_input().split()
k = int(k)
n = int(n)
s = int(s)
p = int(p)


oneperson = (n-1)/s+1
Stotal = oneperson * k
pages=(Stotal-1)/p+1

print (pages)


