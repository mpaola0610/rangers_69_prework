def odd_numbers():
    for num in range(1,100,2):
        print(num)
print(odd_numbers())

def odd_numbers2():
    for num in range(2,101,2):
        print(num)

print(odd_numbers())

def max_num_in_list(a_list):
    max = a_list[0]
    for x in a_list:
        if x > max:
            max = x
    return max
print(max_num_in_list([1,2,3,4,5]))



