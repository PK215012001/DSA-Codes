#  the process of prestoring and fetching the required data to get the frequency of occurences of a character
name = 'djkahffhsdfg'
def prestoring(name):
    hash_dict = {}
    for i in name:
        hash_dict[i] = hash_dict.get(i, 0)+1
    return hash_dict

print(prestoring(name).get('d', 0))