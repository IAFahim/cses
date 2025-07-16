n = int(input())

while True:
    print(n, end=" ")
    if n == 1:
        break
    if not (n & 1):
        n = n // 2
    else:
        n = n * 3 + 1