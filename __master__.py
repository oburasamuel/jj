# asks for the user input
n = int(input("Write a prime number? "))

if n < 2:
    is_prime = False

else:
    is_prime = True

  # checking if the user has entered a prime number by doing the following:
  # i) check if the number is divisible by any integer
  # ii) from 2 to the square root of the number



    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            is_prime = False
              
          
    # should_try = int(input("try again? (y/n): "))
       # if should_try == 'n':
      
  # Display the result
if is_prime:
      print(n, "is a prime number.")
else:
      print(n, "is not a prime number.")


number = int(input("Write a number: "))
n = number

if n < 2:
    is_prime = False

else:
    is_prime = True

    if i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            is_prime = False
        
if is_prime:
    print(n, "is a prime number")

else:
    print(number, "is not a prime number")


