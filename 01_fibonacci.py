import time

def fib_iterative(n):
	if n <= 1:
		return n
	a = 0
	b = 1
	for i in range(1,n):
		sum = a + b
		a = b
		b = sum
	return sum

def fib_recursive(n):
	if n <= 1:
		return n
	if n > 1:
		return fib_recursive(n-2) + fib_recursive(n-1)

start_time = time.time()
for i in range(0,10000):
	fib_iterative(15)
end_time =  time.time()
execution_time = end_time - start_time
print(f"Iterative execution time: {execution_time:.4f}")


start_time = time.time()
for i in range(0,10000):
	fib_recursive(15)
end_time =  time.time()
execution_time = end_time - start_time
print(f"Recursive execution time: {execution_time:.4f}")
