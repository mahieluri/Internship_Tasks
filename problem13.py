# Problem Name: Sherlock and the Valid String
# HackerRank Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter

def isValid(s):
    freq = Counter(s)
    counts = Counter(freq.values())
    
    if len(counts) == 1:
        return "YES"
    if len(counts) > 2:
        return "NO"
    
    # Check if we can remove 1 character to make it valid
    c1, c2 = sorted(counts.items())
    if (c1[0] == 1 and c1[1] == 1) or (c2[0] - c1[0] == 1 and c2[1] == 1):
        return "YES"
        
    return "NO"

if __name__ == '__main__':
    s = input().strip()
    print(isValid(s))