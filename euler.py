

def question1(int):
	ans = sum(x for x in range(int) if (x % 3 == 0 or x % 5 == 0))
	return str(ans)

print(question1(10000))
print(question1(10))

def question2(int):
	ans = 0
	x = 1  
	y = 2  
	while x <= int:
		if x % 2 == 0:
			ans += x
		x, y = y, x + y
	return str(ans)

print(question2(4000000))
print(question2(10000))

import math
def question5(int):
	ans = 1
	for i in range(1, int):
		ans *= i // math.gcd(i, ans)
	return str(ans)

print(question5(29))

def question6(int):
	N = int
	s = sum(i for i in range(1, N + 1))
	s2 = sum(i**2 for i in range(1, N + 1))
	return str(s**2 - s2)

print(question6(10))