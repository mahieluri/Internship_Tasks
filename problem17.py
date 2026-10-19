# Problem Name: Separate the Numbers
# HackerRank Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    if len(s) < 2 or s[0] == '0':
        print("NO")
        return

    for i in range(1, len(s) // 2 + 1):
        first_str = s[:i]
        num = int(first_str)
        built = first_str
        
        while len(built) < len(s):
            num += 1
            built += str(num)
            
        if built == s:
            print(f"YES {first_str}")
            return
            
    print("NO")

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        separateNumbers(input().strip())