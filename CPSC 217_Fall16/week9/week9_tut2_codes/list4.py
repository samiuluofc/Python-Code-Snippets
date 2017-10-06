
def user_input():
    num = []

    n = input("Enter number (between 0 to 100): ")
    while(n != ""):
        num.append(float(n))
        n = input("Enter number (between 0 to 100): ")

    return num


def bubblesort(num):

    for i in range(1,len(num),1):
        for ind in range(0,len(num)-i,1):

            if num[ind+1] < num[ind]:
                temp = num[ind]
                num[ind] = num[ind+1]
                num[ind+1] = temp

    return num



def main():

    num_list = user_input()
    result_list = bubblesort(num_list)
    print(result_list)

main()
        
