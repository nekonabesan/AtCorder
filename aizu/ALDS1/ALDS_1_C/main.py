def isPrime(x):
    if x < 2:
        return 0
    elif x == 2:
        return 1
    elif x % 2 == 0:
        return 0
    i = 3
    while pow(i, 2) <= x:
        if x % i == 0:
            return 0
        i += 2
    return 1

if __name__ == "__main__":
    """
    nums = [2, 3, 4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,17]
    for num in nums:
        if isPrime(num):
            print(f"{num} is a prime number.")
        #else:
        #    print(f"{num} is not a prime number.")
    """
    n=int(input())
    ans=0
    for i in range(n):
        x=int(input())
        if isPrime(x):
            ans+=1
    print(ans)