def selectionSort(array):
    n=len(array)
    for i in range(0,n):
        min_index=i
        for j in range(i+1,n):
            if array[min_index]>array[j]:
                min_index=j
        array[i],array[min_index]=array[min_index],array[i]


n=int(input("How many Element Do you want to Enter : "))
array=[int(input(f"Enter Your Number {i+1} : "))for i in range(n)]

print("Before Sort",format(array))

selectionSort(array)

print("After Sort",format(array))