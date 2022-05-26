import random

# Regular iteration

new_temp = []
temps = [123, 222, 234, 234, 24566]
for temp in temps:
    new_temp.append(temp/10)

print(new_temp)    

# List comperhension

new_temp = [temp/10 for temp in temps]

print(new_temp)    

# List comperhension with if statement
new_temp = [temp/10 for temp in temps if temp != 222]
print(new_temp)

# List comperhension excersize

def remove_strings(initial_list: list):
    return [item for item in initial_list if type(item) == int]
    # another option:
    # return [item for item in initial_list if isinstance(item, int)]

print(remove_strings([234, "asdfa", 9876, "dsssss", 76567, "ddddd"]))

def remove_negative_ints(initial_list: list):
    return [item for item in initial_list if item > 0]

print(remove_negative_ints([234, -4444, 9876, 0, 76567, -234234]))

# List comperhension with if else statement

def replace_negative_ints(initial_list: list):
    return [item if item > 0 else random.randint(1, 9999) for item in initial_list]

print(replace_negative_ints([234, -4444, 9876, 0, 76567, -234234]))

def replace_zeros(initial_list: list):
    return [item if item != 'no data' else 0 for item in initial_list]

print(replace_zeros([234, 'no data', 9876, 0, 76567, 'no data']))

def sum_up(initial_list: list):
    return sum([float(item) for item in initial_list], 0)

print(sum_up(["1.1", '2.2', '3.3']))