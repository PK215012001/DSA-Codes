# Intersection of two sorted arrays with reptition
# brute force approach

arr1 = [1, 1, 2, 3, 4, 4, 5, 6, 7]
arr2 = [1, 2, 4, 4, 6]
temp = []
visited = [0] * len(arr2)
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if(arr1[i] == arr2[j] and visited[j] == 0):
            temp.append(arr1[i])
            visited[j] = 1
            break
        if(arr2[j] > arr1[i]):
            break
print(temp)

# optimal approach
i = 0
j = 0
temp = []
while(i < len(arr1) and j <len(arr2)):
    if(arr1[i] < arr2[j]):
        i += 1
    elif(arr2[j] < arr1[i]):
        j += 1
    else:
        temp.append(arr1[i])
        i += 1
        j += 1
print(temp)