def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-2) + fib(n-1)


# 테스트 코드
for i in range(1, 16):
    print(fib(i))
