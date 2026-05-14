# I don't believe this exercises is present in the exam.
# I was just messing about before attending it
#
# Given a number, write a function that checks if it's prime or not.
# Should return True or False.


def valid_prime(n: int) -> bool:
    if n <= 1:
        return False
    div = 2
    while div < n:
        if n % div == 0:
            return False
        div += 1
    return True

# Another version that returns the next prime if given number wasn'that


def next_prime(n: int) -> str:
    if valid_prime(n):
        return f"{n} is prime!"
    else:
        next_prime = n
        while not valid_prime(next_prime):
            next_prime += 1
    return f"{n} is not prime! Next one is {next_prime}"


print(f"Simple prime check: {valid_prime(11)}")
print(f"Check that finds next prime: {next_prime(12)}")
