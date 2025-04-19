def bubbleSort(arr):
    n=len(arr)
    for k in range(0,n):
        for j in range(0,n-k-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


n=int(input("How many Elements do you want to Enter :"))
my_list=[input(f"Enter element {i+1} :") for i in range(n)]

print("Your list before bubble Sorting :",my_list)

bubbleSort(my_list)

print("Your list after  bubble Sorting :",my_list)

# This is a simple implementation of bubble sort algorithm in Python.
# The function bubbleSort takes a list as input and sorts it in ascending order.