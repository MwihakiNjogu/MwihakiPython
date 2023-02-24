from datetime import date

day_today= date.today().strftime("%A %d %B %Y")
print(day_today)
day= str(input("Enter Today's day:"))
if day == day_today:
    print(f"Today is {day_today}\nCorrect!")

elif day !=day_today:
    print("Your Answer Is Incorrect!\n..Enter the correct day\n:")