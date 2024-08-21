# Functions #
def is_even(number):
    return number % 2 == 0

def is_prime(number):
    if number <= 1:
        return False
    if number == 2: # Exception.
        return True
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

# Main #
def main():
    number = int(input("[SYSTEM] Enter the number: "))
    
    if is_even(number):
        print("[SYSTEM] Number is even!")
    else:
        print("[SYSTEM] Number is odd.")
    
    if is_prime(number):
        print("[SYSTEM] Number is prime!")
    else:
        print("[SYSTEM] Number is not prime.")


# Execute the program #
if __name__ == "__main__":
    main()
