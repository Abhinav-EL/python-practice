import random

print("Hello")

# Defining main function
def main():
    print("hey there -- your number is ", random.randrange(1,10))


# Using the special variable 
# __name__
if __name__=="__main__":
    main()