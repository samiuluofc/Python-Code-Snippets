import sys

# Take inputs and store them in a list
def take_input():
    num_L = []

    while True:
        num = input()
        if num == 'EOF':
            break
        num_L.append(float(num))

    return num_L

# Calculating Geometic mean
def geomean(L):
    multi = 1
    for num in L:
        multi = multi * num

    res = multi ** (1.0/len(L))

    return res

# Calculating Arithmetic mean
def arithmean(L):
    s = 0
    for num in L:
        s = s + num

    res =(s/len(L))

    return res

# Calculating median
def median(L):
    L.sort()
    s = len(L)
    res = []
    if s % 2 == 1:
        res.append(L[int(s/2)])
    else:
        res.append(L[int(s/2)]-1)
        res.append(L[int(s/2)])

    return res


def main():
    
    if len(sys.argv) == 1:
        print("Function name is missing. Provide exactly one function name as argument")

    elif len(sys.argv) > 2:
        print("Too many function names. Provide exactly one function name as argument")

    elif sys.argv[1] == 'geomean':
        numbers = take_input()
        mean_res = geomean(numbers)
        print("Geometric mean: ", round(mean_res,2))

    elif sys.argv[1] == 'median':
        numbers = take_input()
        med_res = median(numbers) 
        print("Median(s): ", med_res)

    elif sys.argv[1] == 'arithmean':
        numbers = take_input()
        mean_res = arithmean(numbers) 
        print("Arithmetic mean: ", mean_res)

    else:
        print("No such function exist.")
    
main()
