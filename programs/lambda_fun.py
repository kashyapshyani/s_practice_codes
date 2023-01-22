# l1 = [1,2,3,4]

# new_l1 = list(filter(lambda x: x%2==0, l1))

# print(new_l1)

factorial  = lambda a: a*factorial(a-1) if (a>1) else 1

number = 6

print('%d != %d' %(number, factorial (number)))

def fibonacci(count):
	fib_list = [0, 1]

	any(map(lambda _: fib_list.append(sum(fib_list[-2:])),
										range(2, count)))

	return fib_list[:count]

print(fibonacci(10))