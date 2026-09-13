print("enter your number:")
seconds = int(input())
days,remainder = divmod(seconds, 24 * 60 * 60)
hours,remainder = divmod(remainder, 60 * 60)
minutes ,remainder = divmod(remainder, 60)

if days % 10 == 1 and days % 100 != 0 and days % 100 !=11:
    days_word ="день"
elif days % 10 in [2,3,4] and days % 100 not in [12,13,14]:
    days_word = "дні"
else:
    days_word = "днів"

if seconds < 0 or seconds >= 8640000:
    print("помилка")

print(f"{days} {days_word} {hours:02d}:{minutes:02d}:{seconds:02d}")