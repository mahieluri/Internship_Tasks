# Problem Name: Making Anagrams
# HackerRank Link: https://www.hackerrank.com/challenges/making-anagrams/problem

from collections import Counter

def makingAnagrams(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    diff = c1 - c2
    diff2 = c2 - c1
    return sum(diff.values()) + sum(diff2.values())

if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()
    print(makingAnagrams(s1, s2))