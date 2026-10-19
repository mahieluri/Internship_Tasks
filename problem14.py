# Problem Name: Anagram
# HackerRank Link: https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1
    mid = len(s) // 2
    s1, s2 = s[:mid], s[mid:]
    c1, c2 = Counter(s1), Counter(s2)
    
    diff = c1 - c2
    return sum(diff.values())

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        print(anagram(input().strip()))