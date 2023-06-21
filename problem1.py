# write a python program to check if a given number is positive or negative 

def main():
    number = int(input("Type a number : "))
    is_positive(number)

def is_positive(n):
    if n > 0 :
        print(f"{n} is positive")
    elif n == 0 :
        print(" 0 is nutre")
    else :
        print(f"{n} is negative")
        
main()