
n = int(input())
a = set(map(int, input().split()))
number_of_operations = int(input())

for _ in range(number_of_operations):
    operation, size = input().split()
    b = set(map(int, input().split()))

    if operation == "intersection_update":
        a.intersection_update(b)
    elif operation == "update":
        a.update(b)
    elif operation == "symmetric_difference_update":
        a.symmetric_difference_update(b)
    elif operation == "difference_update":
        a.difference_update(b)

print(sum(a))
