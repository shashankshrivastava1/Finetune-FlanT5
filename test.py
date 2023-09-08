print("hello world")
# import langchain libraries to make a llm chain with openai
dic = {1: "this is number one", 2: "this is number two", 3: "this is number 3"}
text = "There are some text that needs to be printed here to check that whether the Black formatting is working correctly and break this big text into multiple lines"

print("the value here")
def print_prime_numbers(n):
    # Generate a list of all the numbers from 2 to n
    numbers = [x for x in range(2, n+1)]

    # Use a loop to remove all the numbers that are not prime
    for i in range(2, int(n**0.5)+1):
        if i**2 > n:
            break
        if all([x % i for x in numbers if x != i]):
            numbers.remove(i)

    # Print the prime numbers
    for num in numbers:
        print(num)