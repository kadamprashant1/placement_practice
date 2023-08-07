def bubble(list_arr):

    n=len(list_arr)

    for i in range(n):

        swapped=False #variable to check element is swapped or not

        for j in range(0,n-i-1): #start loop
            if list_arr[j] > list_arr[j+1]:
                list_arr[j],list_arr[j+1]=list_arr[j+1],list_arr[j] #start swapping
                swapped = True
        
        if (swapped==False):
            break

list_arr = [3,1,4,6,7,8,54,34]
print(bubble(list_arr))
for i in range(len(list_arr)):
    print("%d" % list_arr[i], end=" ")
