N = int(input())
year = int(input())
isLeap = int(year % 400 == 0 or year % 4 == 0 and year % 100 != 0)
add = {"January": 0}
add["February"] = add["January"] + 31
add["March"] = add["February"] + 28 + isLeap
add["April"] = add["March"] + 31
add["May"] = add["April"] + 30
add["June"] = add["May"] + 31
add["July"] = add["June"] + 30
add["August"] = add["July"] + 31
add["September"] = add["August"] + 31
add["October"] = add["September"] + 30
add["November"] = add["October"] + 31
add["December"] = add["November"] + 30
Holidays = [0] * 7
for _ in range(N):
    day, month = map(str, input().split())
    day = int(day)
    Holidays[(day + add[month]) % 7] += 1
alias = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    0: "Sunday",
}
adjust = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}
day_of_week = input()
Holidays[1] -= 1
if isLeap: Holidays[2] -= 1
bestDay = Holidays.index(min(Holidays))
worstDay = Holidays.index(max(Holidays))
print(alias[(bestDay + adjust[day_of_week]) % 7], alias[(worstDay + adjust[day_of_week]) % 7])
