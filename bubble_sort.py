# sorting an array happens by pushing the maximum to last by adjacent swappings
# swap count will make it optimised for bubble sort
num_list = [25, 87, 102, 15, 2, 32]
for i in range(len(num_list)-1):
    swap_count = 0
    for j in range(len(num_list) - i - 1):
        if (num_list[j] > num_list[j+1]):
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
            swap_count = 1
    if (swap_count == 0):
        break
print(num_list)