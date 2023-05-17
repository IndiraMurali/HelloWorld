def hello():
    return f"This is my first Hello world program"


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b



def hi():
    return f"Inside Hi Function"

if __name__ == "__main__":
    print("Inside Main Function")
    print("I am updating back to github")
    obj = hello()
    #hi()
    print(obj)
    inp1 = int(input("Enter Your Input 1 : "))
    inp2 = int(input("Enter Your Input 2 : "))
    print(f"Addition Results : ", add(inp1, inp2))
    print(f"Subtraction Results : ", sub(inp1, inp2))
    print(f"Multiplication Results : ", mul(inp1, inp2))
