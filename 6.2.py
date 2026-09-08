seconds = int(input())

days = seconds // 86400
seconds %= 86400

hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

print(f"{days} дні, {hours:02}:{minutes:02}:{seconds:02}")