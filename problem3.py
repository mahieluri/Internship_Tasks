# Problem Name: Mars Exploration
# HackerRank Link: https://www.hackerrank.com/challenges/mars-exploration/problem

s = input().strip()
expected = "SOS" * (len(s) // 3)
print(sum(1 for i in range(len(s)) if s[i] != expected[i]))