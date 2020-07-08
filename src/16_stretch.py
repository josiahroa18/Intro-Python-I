def is_prime(num):
    num = int(num)
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False

def main():
    num = input("Please input a number you want to check: ")
    if is_prime(num):
        print(f"{num} is a prime number!")
    else:
        print(f"{num} is not a prime number")

if __name__ == "__main__":
    main()