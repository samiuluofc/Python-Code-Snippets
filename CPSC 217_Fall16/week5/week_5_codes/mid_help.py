import math

num = float(input())
limit = math.floor(math.sqrt(num/2))

for i in range(0,limit+1,1):
    right = num - (i * i)
    sq = math.sqrt(right)

    if(sq == math.ceil(sq)):
        print(int(num)," = ", i, " * ", i," + ",int(sq)," * ", int(sq))    



