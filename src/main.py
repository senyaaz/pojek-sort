from sorter import generate_random_array, quick_sort
from analyzer import split_array, compare_halves, print_analysis

def main():

    print("=" * 50)
    print("ПРОГРАММА: СОРТИРОВКА И АНАЛИЗ МАССИВА")
    print("=" * 50)
    
    print("\n1. Генерируем случайный массив из 10 чисел...")
    arr = generate_random_array(10)
    print(f"   Исходный массив: {arr}")
    
    print("\n2. Сортируем массив (быстрая сортировка)...")
    sorted_arr = quick_sort(arr)
    print(f"   Отсортированный массив: {sorted_arr}")
    
    print("\n3. Делим массив на две половины...")
    first_half, second_half = split_array(sorted_arr)
    print(f"   Первая половина: {first_half}")
    print(f"   Вторая половина: {second_half}")
    
    print("\n4. Анализируем половины...")
    results = compare_halves(first_half, second_half)
    print_analysis(results)
    
    print("\n" + "=" * 50)
    print("ПРОГРАММА ЗАВЕРШЕНА УСПЕШНО!")
    print("=" * 50)

if __name__ == "__main__":
    main()
