
# Problem 16: Nested Lists
# HackerRank: https://www.hackerrank.com/challenges/nested-list/problem

students = []

n = int(input())

for i in range(n):
    name = input().strip()
    score = float(input())
    students.append([name, score])

scores = sorted(set(student[1] for student in students))
second_lowest = scores[1]

names = sorted(
    student[0] for student in students
    if student[1] == second_lowest
)

for name in names:
    print(name)
