def quick_sort(arr):
    """Быстрая сортировка массива."""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def generate_array(size=10):
    """Генерирует случайный массив."""
    import random
    return [random.randint(1, 100) for _ in range(size)]
