def hello():
    return f"This is my first Hello world program"

def hi():
    return f"Inside Hi Function"

if __name__ == "__main__":
    print("Inside Main Function")
    obj = hello()
    hi()
    print(obj)
