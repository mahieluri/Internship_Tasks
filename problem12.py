
# Problem 12: Introduction to Sets
# HackerRank: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

n = int(input())
heights = list(map(int, input().split()))

unique_heights = set(heights)
average = sum(unique_heights) / len(unique_heights)

print(round(average, 3))
