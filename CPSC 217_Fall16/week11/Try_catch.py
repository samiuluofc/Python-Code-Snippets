



def main():
    try:
        file_in = input("Enter file name: ")
        file_h1 = open(file_in,"r")

        all_input = file_h1.read()
        
        list_number = all_input.split(" ")
        sum = 0
        x = 10/0;
        for i in range(0,len(list_number)):
            sum = sum + float(list_number[i])

      

        res = sum / len(list_number)
        
        file_out = file_in[:file_in.find(".")] + ".out"
        
        file_h2 = open(file_out,"w")

        str1 = "Average of " + str(len(list_number)) + " numbers is :" + str(res) +".\n"

        file_h2.write(str1)

        file_h1.close()
        file_h2.close()

    
    #except Exception:
        #print("Runtime errors.............")
        #print("Check your code under try block")
    except ZeroDivisionError:
        print("Divide by zero errors")
    except ValueError:
        print("Value error")
	
        
main()

#Other buitin exceptions are: https://docs.python.org/2/library/exceptions.html
