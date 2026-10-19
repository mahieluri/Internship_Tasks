# Problem Name: Weighted Uniform Strings
# HackerRank Link: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

def weightedUniformStrings(s, queries):
    weights = set()
    current_weight = 0
    prev_char = ''
    
    for char in s:
        weight = ord(char) - ord('a') + 1
        if char == prev_char:
            current_weight += weight
        else:
            current_weight = weight
            prev_char = char
        weights.add(current_weight)
        
    return ["Yes" if q in weights else "No" for q in queries]

if __name__ == '__main__':
    s = input().strip()
    n = int(input())
    queries = [int(input()) for _ in range(n)]
    print('\n'.join(weightedUniformStrings(s, queries)))