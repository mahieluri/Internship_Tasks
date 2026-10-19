
a = set(map(int, input().split()))
n = int(input())

result = True

for _ in range(n):
    b = set(map(int, input().split()))

    if not a > b:
        result = False
        break

print(result)
