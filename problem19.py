
# Problem 19: Collections.Counter()
# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

x = int(input())
sizes = list(map(int, input().split()))
shoe_counts = Counter(sizes)

n = int(input())
earnings = 0

for i in range(n):
    size, price = map(int, input().split())

    if shoe_counts[size] > 0:
        earnings += price
        shoe_counts[size] -= 1

print(earnings)
