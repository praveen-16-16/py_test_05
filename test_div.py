import pytest
from arithmetics import divide

def test_divide():
    result1 = divide(6, 2)
    result2 = divide(5, 2)
    
    print(f"Division Results: {result1}, {result2}")

    assert result1 == 3
    assert result2 == 2.5
    
    with pytest.raises(ValueError):
        divide(10, 0)
