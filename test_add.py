from arithmetics import add

def test_add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = add(a,b)

    print(f"\nResult of Addition ({a}, {b}) = {result}")
