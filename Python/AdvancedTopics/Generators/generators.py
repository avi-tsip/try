# Regular Loop

def square_me(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_square = square_me([1,2,3,4,5])
print(my_square)

# Doing it the generator way

def square_generator(nums):
    for i in nums:
        yield (i*i)

my_square = square_generator([1,2,3,4,5])

# Check out the print statement when using yield
for num in my_square:
    print(num)

# Try the same example with list comprehension

new_list = [x*x for x in [1,2,3,4,5]]
print(new_list)

# Or, use it like with generator with paranthesis instead of brackets

new_list = (x*x for x in [1,2,3,4,5])

print(type(new_list))
for num in new_list:
    print(num)

# I can convert a generator back to list like this
last_list = list(new_list)
print(type(last_list))