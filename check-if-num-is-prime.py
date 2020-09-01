if __name__ == '__main__':
    num = int(input('Enter a number '))
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            print('Not a prime number')
            break

    if isPrime:
        print('is a prime number')
