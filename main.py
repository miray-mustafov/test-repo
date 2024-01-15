def is_prime(a):
    if a <= 1:
        return False
    elif a == 2:
        return True
    elif a % 2 == 0:
        return False
    for i in range(3, int(a ** 0.5) + 1, 2):
        if a % i == 0:
            return False
    return True


print('Hi')
a = 5
is_a_prime = is_prime(a)
if is_a_prime:
    print('a is prime yes')
else:
    print('No')
