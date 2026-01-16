# Bubble Sort Program

arr = [5, 3, 8, 2, 1]

n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            # swap
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array:", arr)
