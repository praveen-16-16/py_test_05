from arithmetics import add

def addd():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = add(a,b)

    print(f"\nResult of Addition ({a}, {b}) = {result}")

def test_add():
    a = 5
    b = 10

    result = add(a,b)

    print(f"\nResult of Addition ({a}, {b}) = {result}")
