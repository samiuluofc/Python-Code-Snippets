# Find geometric mean and median of N numbers


# Take inputs and store them in a list
def take_input():
    num_L = []

    while True:
        num = input()
        if num == 'EOF':
            break
        num_L.append(float(num))

    return num_L

# Calculating Geometric mean
def geo_mean(L):
    multi = 1
    for num in L:
        multi = multi * num

    res = multi ** (1.0/len(L))

    return res

# Calculating Median 
def my_med(L):
    L.sort()
    s = len(L)
    res = []
    if s % 2 == 1:
        res.append(L[int(s/2)])
    else:
        res.append(L[int(s/2)]-1)
        res.append(L[int(s/2)])

    return res

% Main function
def main():
    numbers = take_input()
    mean = geo_mean(numbers)
    print("Geometric mean: ", round(mean,2))
    m_res = my_med(numbers) 
    print("Median(s): ", m_res)
    
main()
