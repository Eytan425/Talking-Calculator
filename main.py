import pyttsx3

def Add(x,y):
    return x+y
def Subtract(x,y):
    return x - y
def Multiply(x,y):
    return x*y
def Divide(x, y):
    return x / y

    

def main():
    num1 = int(input("Enter the first number (This number is greater than the second one): "))
    num2 = int(input("Enter the second number(This number is smaller than the first one ): "))
    print("Choose: ")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    operator = int(input("Enter the number representing the operator (1,2,3,4): "))
    if operator in [1,2,3,4]:
        
        if(operator == 1):
            answer = Add(num1, num2)
            engine = pyttsx3.init()
            engine.say(answer)
            engine.runAndWait()
        elif(operator == 2):
            answer = Subtract(num1, num2)    
            engine = pyttsx3.init()
            engine.say(answer)
            engine.runAndWait()
        elif(operator == 3):
            answer = Multiply(num1, num2)
            engine = pyttsx3.init()
            engine.say(answer)
            engine.runAndWait()
        elif(operator == 4):
            answer = Divide(num1, num2)
            engine = pyttsx3.init()
            engine.say(answer)  
            engine.runAndWait()      
    else:
        print(f"The number {operator} isn't representing any operator")

if __name__ == "__main__":
    main()            
    