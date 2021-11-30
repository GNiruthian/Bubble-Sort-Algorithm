arr = [15, 234, 89, 21 , 27 ,17 , 4, 0 ,58]

for j in range(0, len(arr)):
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]

for i in range(0, len(arr)):
    print(arr[i])

    # Bubble Sort