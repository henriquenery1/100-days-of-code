def is_prime(base_number):
    base_number = int(base_number)
        
    for i in range(2, base_number):
        if base_number % i == 0:
            return False

    return True        


def find_next_prime(base_number):
    base_number = int(base_number)
    not_find_prime = True

    while not_find_prime:
        if is_prime(base_number):
            return base_number
        else:
            base_number += 1
            print(base_number)