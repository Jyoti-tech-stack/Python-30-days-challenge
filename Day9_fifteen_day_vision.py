name = "Jiya"
days = int(input("Kitne din ka streak chahiye? "))
favourite_number = 7

for day in range(1, days + 1):
    if day == favourite_number:
        print(f"{name} Day {day} - LUCKY DAY 🍀 Maza double")
    elif day <= 8:
        print(f"{name} Day {day} - DONE ✅ Maza aa gaya")
    else:
        print(f"{name} Day {day} - TARGET 🎯 Fod denge")
        
print(f"{name} {days} Day streak ki taraf badh rahi hai!")
print("Day 9 Complete by Jyoti-tech-stack 💪")
