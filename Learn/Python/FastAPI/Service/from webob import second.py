from webob import second


int_list = [7, 19, 2334, 12, 165]
i = 0
highest_number = 0
second_highest = 0
temp_second_highest = 0
while i < len(int_list) - 1:

    highest_number = max(int_list[i],  int_list[i+1])
    temp_second_highest = min(int_list[i],  int_list[i+1])
    if temp_second_highest > second_highest:
        second_highest = temp_second_highest
    i += 1

print(highest_number)
print(second_highest)