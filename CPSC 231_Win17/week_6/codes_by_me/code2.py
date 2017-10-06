

def boardprint(mat):
    for row in mat:
        for col in row:
            if col == 1:
                print('X',end = '')
            else:
                print('_',end = '')
        print()

def boardprint_rev(mat):
    for r in range(len(mat)-1,-1,-1):
        for c in mat[r]:
            if c == 1:
                print('X',end = '')
            else:
                print('_',end = '')
        print()

def boardswap(mat):
    i = 0
    j = len(mat)-1

    while i < j:
        temp = mat[i]
        mat[i] = mat[j]
        mat[j] = temp
        i = i + 1
        j = j - 1 

def main():
    bm = [[ 0, 1, 1, 0 ],[ 1, 1, 1, 1 ],[ 1, 0, 0, 0 ],\
      [ 1, 0, 0, 1 ],[ 0, 1, 1, 0 ]]
    
    boardprint(bm)
    print("-------------")
    boardswap(bm)
    boardprint(bm)
    print("-------------")
    
main()
