import datetime as dt

print(dt.datetime.now().strftime("%Y-%m-%d в %H:%M:%S"))
arr = ["12-07-2023", "11-07-2023", "10-07-2023", "09-07-2023"]
print(list(filter(lambda x: x == "12-07-2023", arr)))
