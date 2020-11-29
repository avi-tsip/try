import time
import asyncio

def is_prime(x):
    return not any(x//i == x/i for i in range(x-1,1,-1))

async def highest_prime_below(num):
    print(f'highest prime number below {num}')
    for y in range(num-1,0,-1):
        if is_prime(y):
            print(f'highest prime number below {num} is {y}')
            return y
        await asyncio.sleep(0.01)
    return None


async def main():
    await asyncio.wait([
    highest_prime_below(1000000),
    highest_prime_below(10000),
    highest_prime_below(1000)
    ])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
