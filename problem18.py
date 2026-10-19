# Problem Name: String Construction
# HackerRank Link: https://www.hackerrank.com/challenges/string-construction/problem

def stringConstruction(s):
    return len(set(s))

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        print(stringConstruction(input().strip()))