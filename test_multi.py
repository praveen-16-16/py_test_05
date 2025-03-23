from arithmetics import multiply

def test_add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = multiply(a,b)

    print(f"\nResult of Multiplye ({a}, {b}) = {result}")
