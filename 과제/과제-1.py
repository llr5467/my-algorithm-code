import time
import random
import math

# 1. 삽입 정렬 (Insertion Sort)
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 2. 쉘 정렬 (Shell Sort - Knuth Sequence)
def shell_sort(arr):
    arr = arr.copy()
    n = len(arr)
    gap = 1
    while gap < n // 3:
        gap = 3 * gap + 1

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 3
    return arr

# 3. 큐브 정렬 시뮬레이션 (Cube Sort Simulation)
def cube_sort(arr):
    arr = arr.copy()
    n = len(arr)
    if n <= 1:
        return arr

    # 다차원 큐브 분할 (d-dimensional cube simulation)
    dim = max(2, int(math.ceil(math.log2(n) / 2)))
    side = int(math.ceil(n ** (1.0 / dim)))

    # 큐브 축 기준 서브 배열 분할 및 정렬
    sub_size = max(1, n // side)
    sub_cubes = [arr[i:i + sub_size] for i in range(0, n, sub_size)]

    # 각 서브 큐브 정렬
    sorted_cubes = [sorted(cube) for cube in sub_cubes]

    # 병합 함수 (Merge Two)
    def merge_two(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # 다차원 머지 단계 (Merge Cubes)
    def merge_cubes(cubes):
        while len(cubes) > 1:
            next_cubes = []
            for i in range(0, len(cubes), 2):
                if i + 1 < len(cubes):
                    next_cubes.append(merge_two(cubes[i], cubes[i+1]))
                else:
                    next_cubes.append(cubes[i])
            cubes = next_cubes
        return cubes[0]

    return merge_cubes(sorted_cubes)

# 4. 성능 테스트 실행 함수 (Benchmark Function)
def benchmark():
    sizes = [1000, 3000, 5000]
    print(f"{'Data Size':<10} | {'Insertion (s)':<15} | {'Shell (s)':<15} | {'Cube (s)':<15}")
    print("-" * 65)

    for size in sizes:
        data = [random.randint(0, 100000) for _ in range(size)]

        # Insertion Sort
        t0 = time.perf_counter()
        insertion_sort(data)
        t_ins = time.perf_counter() - t0

        # Shell Sort
        t0 = time.perf_counter()
        shell_sort(data)
        t_shell = time.perf_counter() - t0

        # Cube Sort
        t0 = time.perf_counter()
        cube_sort(data)
        t_cube = time.perf_counter() - t0

        print(f"{size:<10} | {t_ins:<15.5f} | {t_shell:<15.5f} | {t_cube:<15.5f}")

if __name__ == "__main__":
    benchmark()
