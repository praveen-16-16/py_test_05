from arithmetics import multiply

def test_multiply():
    result1 = multiply(3, 2)
    result2 = multiply(-1, 3)
    result3 = multiply(0, 5)
    
    print(f"Multiplication Results: {result1}, {result2}, {result3}")

    assert result1 == 6
    assert result2 == -3
    assert result3 == 0
