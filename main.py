def add(x, y):
    result = x + y
    print(f"DEBUG: adding {x} + {y} = {result}")
    return result

def subtract(x, y):
    return x - y

if __name__ == "__main__":
    print("Simple Calculator")
    print(f"10 + 5 = {add(10, 5)}")
