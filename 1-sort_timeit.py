import random
import timeit

# Функція сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Функція сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Підготовка наборів даних
sizes = [100, 1000, 5000, 10000]
test_data = {size: [random.randint(0, 10000) for _ in range(size)] for size in sizes}

# Вимірювання часу виконання
results = {}
for size in sizes:
    arr = test_data[size]
    time_insertion = timeit.timeit('insertion_sort(arr[:])', globals=globals(), number=1)
    time_merge = timeit.timeit('merge_sort(arr[:])', globals=globals(), number=1)
    time_timsort = timeit.timeit('sorted(arr)', globals=globals(), number=1)
    results[size] = (time_insertion, time_merge, time_timsort)

# Вивід результатів
for size in sizes:
    print(f"Розмір масиву: {size}:")
    print(f"Сортування вставками: {results[size][0]:.6f} сек")
    print(f"Сортування злиттям: {results[size][1]:.6f} сек")
    print(f"Timsort: {results[size][2]:.6f} сек")
    print()