from arithmetics import divide

def test_add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = divide(a,b)

    print(f"\nResult of Divide ({a}, {b}) = {result}")
