
def partition(array,lb,ub):
    pivot = array[lb]
    start = lb
    end = ub

    while True:
        while start <= end and array[start] <= pivot:
            start = start+1

        while start <= end and array[end] > pivot:
            end = end-1

        if start<end:
            array[start],array[end]=array[end],array[start]

        else:
            break

    array[lb],array[end]=array[end],array[lb]
    return end

def quickSort(array,start,end):
    if start >= end:
        return
    
    k = partition(array, start, end)
    quickSort(array, start, k-1)
    quickSort(array, k+1, end)


n=int(input("How many element : "))
data=[int(input(f"Enter your number {i+1} : ")) for i in range(n)]

print("Before sorting : ",format(data))

lb = 0
ub = len(data)-1
quickSort(data, lb, ub)

print("Aftere sorting : ",format(data))
