# Problem Name: Caesar Cipher
# HackerRank Link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

def caesarCipher(s, k):
    result = []
    for char in s:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = chr(start + (ord(char) - start + k) % 26)
            result.append(shifted)
        else:
            result.append(char)
    return "".join(result)

if __name__ == '__main__':
    n = int(input())
    s = input()
    k = int(input())
    print(caesarCipher(s, k))