import time

def is_prime(x):
    return not any(x//i == x/i for i in range(x-1,1,-1))

def highest_prime_below(num):
    print(f'highest prime number below {num}')
    for y in range(num-1,0,-1):
        if is_prime(y):
            print(f'highest prime number below {num} is {y}')
            return y
        time.sleep(0.01)
    return None


def main():
    highest_prime_below(1000000)
    highest_prime_below(10000)
    highest_prime_below(1000)

main()