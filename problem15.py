# Problem Name: Game of Thrones - I
# HackerRank Link: https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter

def gameOfThrones(s):
    counts = Counter(s)
    odd_count = sum(1 for count in counts.values() if count % 2 != 0)
    return "YES" if odd_count <= 1 else "NO"

if __name__ == '__main__':
    s = input().strip()
    print(gameOfThrones(s))