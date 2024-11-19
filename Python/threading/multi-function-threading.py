from concurrent.futures import ThreadPoolExecutor

def method1(x,y):
     calc = x*y
     print(calc)

def method2(x,y):
     calc = x+y
     print(calc)

def method3(x,y):
     calc = x-y
     print(calc)

pool = ThreadPoolExecutor(max_workers=3)
x = 5
y = 6
pool.submit(method1, x, y)
pool.submit(method2, x, y)
pool.submit(method3, x, y)