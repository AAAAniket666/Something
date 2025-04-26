# Selection Sort implementation in Python

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers to sort (space separated): ").split()))
    selection_sort(arr)
    print("Sorted array:", arr)