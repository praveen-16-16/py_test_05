

from arithmetics import subtract

def test_sub():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = subtract(a,b)

    print(f"\nResult of subtract ({a}, {b}) = {result}")

