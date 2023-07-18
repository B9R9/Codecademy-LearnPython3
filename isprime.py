def isprime(num):
	if num == 2 or num == 3: return True
	if num % 2 == 0 or num < 2 : return False
	for i in range(3, num, 2):
		if num % i == 0: return False
	return True

prime_numbers_list = filter(isprime, range(0,100))
for x in prime_numbers_list:
  print(x)

for x in range(0, 20):
	if isprime(x):
		print(f"{x} is a prime number")
	else:
		print(f"{x} is not a prime Number")
	
