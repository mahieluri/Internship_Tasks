# Problem Name: Gemstones
# HackerRank Link: https://www.hackerrank.com/challenges/gem-stones/problem

def gemstones(arr):
    gem_set = set(arr[0])
    for s in arr[1:]:
        gem_set.intersection_update(set(s))
    return len(gem_set)

if __name__ == '__main__':
    n = int(input())
    arr = [input().strip() for _ in range(n)]
    print(gemstones(arr))