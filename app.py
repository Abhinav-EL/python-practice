import random

print("Hello")

# Defining main function
def main():
    print("hey there -- your number is ", random.randrange(1,1000))
    x = ["apple", "banana", "cherry", "berry"]
    y = [item for item in x if "a" not in item]
    y.sort(reverse=True)
    #for i in y:
    #    print(i)

    #objList = [{"a":1, "b":2}, {"a":10, "b":20}]
    #for i in objList:
    #    print(i)

    d1 = dict(a=1, b=2, c=3)
    d2 = {d:d1[d]*2 for d in d1} #dictionary comprehension
    for k,v in d2.items():
        print(k, " - ", v)

# Using the special variable 
# __name__
if __name__=="__main__":
    main()