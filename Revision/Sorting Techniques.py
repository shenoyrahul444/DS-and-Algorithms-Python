"Bubble sort"
"Swapping adjacent elements"

def bubble_sort(alist):

    n = len(alist)

    for i in range(n):
        for j in range(n-1-i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]


def insertion_sort(alist):
    n = len(alist)
    for i in range(1,n):
        element = alist[i]
        j = i
        while alist[j-1] > element and j>0:
            alist[j] = alist[j-1]
            j -= 1

        alist[j] = element


def merge_sort(alist):
    n = len(alist)
    if n > 1:
        mid = n//2
        left = alist[:mid]
        right = alist[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i]< right[j]:
                alist[k] = left[i]
                i+=1
                k+=1
            elif right[j] < left[i]:
                alist[k] = right[j]
                j+=1
                k+=1
            elif left[i] == right[j]:
                alist[k] = left[i]
                i+=1
                k += 1

                alist[k] = right[j]
                k+=1
                j+=1

        while i < len(left):
            alist[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            alist[k] = right[j]
            j+=1
            k+=1



def quick_sort(alist):

    n  = len(alist)
    _quicksort(alist,0,n-1)
def partition(alist,low,high):
    if low < high:
        i = (low - 1)
        pivot = alist[high]
        for j in range(low,high):
            if alist[j] <= pivot:
                i+=1
                alist[j],alist[i] = alist[i],alist[j]

        alist[i+1],alist[high] = alist[high],alist[i+1]

    return (i+1)
def _quicksort(alist,low,high):

    if low < high:
        pi = partition(alist,low,high)
        _quicksort(alist,0,pi-1)
        _quicksort(alist,pi+1,high)

arr = [8,1,4,2,7,9,3]
print(arr)
# bubble_sort(arr)
# insertion_sort(arr)
# merge_sort(arr)
quick_sort(arr)

print(arr)
