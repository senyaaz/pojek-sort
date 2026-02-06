import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def main():
    print("=== ПРОГРАММА ЗАПУЩЕНА ===")
    
    arr = [random.randint(1, 100) for _ in range(8)]
    print(f"Исходный: {arr}")
    
    sorted_arr = quick_sort(arr)
    print(f"Отсортированный: {sorted_arr}")
    
    mid = len(sorted_arr) // 2
    first = sorted_arr[:mid]
    second = sorted_arr[mid:]
    
    print(f"\nПервая половина: {first}")
    print(f"Вторая половина: {second}")
    
    sum_first = sum(first)
    sum_second = sum(second)
    
    print(f"\nСумма первой: {sum_first}")
    print(f"Сумма второй: {sum_second}")
    
    if sum_first > sum_second:
        print("Вывод: Первая половина больше")
    else:
        print("Вывод: Вторая половина больше")

if __name__ == "__main__":
    main()
