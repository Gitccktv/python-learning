print("输入你的出生日期")
year=int(input("年份："))
month=int(input("月份："))
day=int(input("日："))

age=2026-year
if month>8 or (month==8 and day>11):
    age-=1
print(f"你的年龄是{age}岁")