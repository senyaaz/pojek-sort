from src.sorter import quick_sort

def test_empty():
    assert quick_sort([]) == []

def test_single():
    assert quick_sort([5]) == [5]

def test_sorted():
    assert quick_sort([1, 2, 3]) == [1, 2, 3]

def test_reverse():
    assert quick_sort([3, 2, 1]) == [1, 2, 3]

if __name__ == "__main__":
    test_empty()
    test_single()
    test_sorted()
    test_reverse()
    print("Все тесты пройдены! ✅") 
