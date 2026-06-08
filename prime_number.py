def find_primes(limit):
   
    primes = []
    
    # 0 and 1 are not prime numbers, so we start at 2
    for num in range(2, limit + 1):
        is_prime = True

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break 
        if is_prime:
            primes.append(num)
            
    return primes

print(find_primes(50))