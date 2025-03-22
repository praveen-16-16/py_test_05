from arithmetics import subtract

def test_subtract():
    result1 = subtract(5, 2)
    result2 = subtract(2, 5)
    result3 = subtract(0, 0)
    
    print(f"Subtraction Results: {result1}, {result2}, {result3}")

    assert result1 == 3
    assert result2 == -3
    assert result3 == 0
