import re

n = int(input())

for _ in range(n):
    phone = input()

    if re.fullmatch(r"[789]\d{9}", phone):
        print("YES")
    else:
        print("NO")
