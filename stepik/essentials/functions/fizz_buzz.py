def generate_fizz_buzz_list(number:int) -> list:
    return ['Fizz'*(not n%3) + 'Buzz'*(not n%5) or n for n in range(1,number+1)]

print(generate_fizz_buzz_list(20))