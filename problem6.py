# Problem Name: Pangrams
# HackerRank Link: https://www.hackerrank.com/challenges/pangrams/problem

import string

def pangrams(s):
    alphabet = set(string.ascii_lowercase)
    s_set = set(s.lower())
    return "pangram" if alphabet.issubset(s_set) else "not pangram"

if __name__ == '__main__':
    print(pangrams(input()))