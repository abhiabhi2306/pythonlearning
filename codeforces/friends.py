input1 = int(input())
input2 = int(input())
points = abs((input1 - input2))
temp = points/2
answer = temp*(temp+1)
if (points & 1):
    answer += (temp+1)


print (answer)
