n = int(input())
res = 1

for i in range(n):
    num = float(input())
    res = res * num

exp = 1/float(n)
geo_mean = res ** exp
print('Geometric mean: ', geo_mean)


