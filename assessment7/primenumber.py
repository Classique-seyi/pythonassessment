
def prime_number(n):
    
    if n < 2:
        return False
  
    for i in range (2, n):

        if n%i == 0:
            return False
        
    return True

def prime_up_to_n(n):
    num_list = []

    for i in range(2, n):
        if prime_number(i):
            num_list.append(i)
    return num_list
   

def sum_primes(n):
    num = prime_up_to_n(n)
    total = 0

    for n in num:
        total += n
    return total


n = 27
if prime_number(n):
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")

print(prime_up_to_n(n))
print(sum_primes(n))

# n = int(input())

# num_list = []
# for i in range (2, n):
#     if n%i != 0:
#         num_list.append(i)
#         print(f"{n} is prime")
       
#     print(f"{n} is not prime")
# print(num_list) 