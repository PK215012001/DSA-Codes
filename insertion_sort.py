# sorts the arry by placing the elementg in it's correct position
num_list = [25, 87, 102, 15, 2, 32]
for i in range(1, len(num_list)):
    for j in range(i, 0, -1):
        if (num_list[j] < num_list[j-1]):
            num_list[j], num_list[j-1] = num_list[j-1], num_list[j]
        else:
            break
print(num_list)