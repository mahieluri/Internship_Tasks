# Problem Name: The Captain's Room
# HackerRank Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem

k = int(input())
rooms = list(map(int, input().split()))

room_set = set(rooms)
sum_set_sum = sum(room_set) * k
sum_rooms = sum(rooms)

captain_room = (sum_set_sum - sum_rooms) // (k - 1)
print(captain_room)