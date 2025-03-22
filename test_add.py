from arithmetics import add

def test_add():
    result1 = add(3, 2)
    result2 = add(-1, 1)
    result3 = add(0, 0)
    
    print(f"Addition Results: {result1}, {result2}, {result3}")  # Print output

    assert result1 == 5
    assert result2 == 0
    assert result3 == 0
