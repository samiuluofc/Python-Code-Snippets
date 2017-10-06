# Find geometric mean of N numbers


# Take inputs and store them in a list
num_L = []

while True:
    num = input()
    if num == 'EOF':
        break
    num_L.append(float(num))

# Calculating Geometric mean
multi = 1
for num in num_L:
    multi = multi * num

res = multi ** (1.0/len(num_L))

print("Geometric mean: ", round(res,2))
