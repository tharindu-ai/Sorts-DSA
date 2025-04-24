def insertionSort(array):
    n=len(array)
    for i in range(1, n):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key

n=int(input("Enter Your Number : "))
array=[int(input(f"Enter number {i+1} : ")) for i in range(n)]

print("Before in sorting : ",format(array))
insertionSort(array)
print("After  in sorting  : ",format(array))