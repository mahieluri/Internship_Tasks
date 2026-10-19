# Problem Name: Alternating Characters
# HackerRank Link: https://www.hackerrank.com/challenges/alternating-characters/problem

def alternatingCharacters(s):
    deletions = 0
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            deletions += 1
    return deletions

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        print(alternatingCharacters(input().strip()))