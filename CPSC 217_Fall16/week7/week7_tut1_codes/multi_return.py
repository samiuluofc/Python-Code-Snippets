# Calculate the addition, subtraction and multiplication of two numbers.

# Calculate the result based on user choice
# Parameters:
#   a: The first integer
#   b: The second integer
#   c: Choice of the user
# Returns: The result
def calculate(a, b):
    x = a + b
    y = a - b
    z = a * b

    return x, y, z # return multiple values



def main():
  # Read the choice integers from the user
  a = int(input("Enter the value of a: "))
  b = int(input("Enter the value of b: "))

  # calculate the result based on user choice
  add, sub, mul = calculate(a, b)
  print("The addition of:",a,"and",b,"is", add)
  print("The subtraction of:",a,"and",b,"is", sub)
  print("The multiplication of:",a,"and",b,"is", mul)

main()
