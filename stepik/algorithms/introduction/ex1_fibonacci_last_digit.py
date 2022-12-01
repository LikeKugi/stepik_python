#  необходимо найти последнюю цифру nn-го числа Фибоначчи.

def fib_digit(n):
    f0, f1 = 0, 1
    for _ in range(n - 1):
        f0, f1 = f1 % 10, (f0 + f1) % 10
    return f1 % 10


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
