#create function that user inputs his age
#function prints number of months lived


def calculate_months():
    age = int(input("enter your age"))
    months_lived = age * 12
    print(f"you have lived{months_lived}months")

calculate_months()
