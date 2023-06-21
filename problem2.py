# this code convert temperatures to and from celsius, fahrenheit.

def main():
    choice = choose()
    if choice == 1:
        temp = celsius(float(input("Type the temperature in celsius: ")))
        print(f"Temperature in Fahrenheit is {temp}")
    elif choice == 2:
        temp = fahrenheit(float(input("Type the temperature in fahrenheit: ")))
        print(f"Temperature in Celsius is {temp}")
    else :
        print("Oops , you typed an invalid number .")
 
def choose():
    print("Choose what do you want ? ")
    print(" 1. from celsius to fahrenheit ")
    print(" 2. from fahrenheit to celsius")
    return (int(input("type 1 or 2 : ")))

def celsius(temp):
    return (temp * 1.8) + 32

def fahrenheit(temp):
    return (temp - 32) * .5556
    
main() 