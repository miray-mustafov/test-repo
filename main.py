def is_prime(a):
    for i in range(3, int(a ** 0.5) + 1, 2):
        if a % i == 0:
            return False
    return True


print('Hi')

is_a_prime = is_prime(a)
if is_a_prime:
    print('a is prime yes')
else:
    print('No')
