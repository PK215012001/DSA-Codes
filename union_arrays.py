# Union of 2 arrays 
# Brute force approach

arr1 = [1, 1, 2, 3, 4, 4, 4, 5]
arr2 = [2, 3, 4, 5, 6]
combined_set = set(arr1+arr2)
sorted_list = sorted(list(combined_set))
print(sorted_list)

# optimal solution using two pointer approach
temp = []
i = 0
j = 0
while (i < len(arr1) and j < len(arr2)):
    if (arr1[i] <= arr2[j]):
        if (len(temp) == 0 or temp[-1] != arr1[i]):
            temp.append(arr1[i])
        i += 1
    else:
        if(len(temp) == 0 or temp[-1] != arr2[j]):
            temp.append(arr2[j])
        j += 1
    
while(i < len(arr1)):
    if (len(temp) == 0 or temp[-1] != arr1[i]):
        temp.append(arr1[i])
    i+=1
while(j < len(arr2)):
    if(len(temp) == 0 or temp[-1] != arr2[j]):
        temp.append(arr2[j])
    j += 1

print(temp)

            
