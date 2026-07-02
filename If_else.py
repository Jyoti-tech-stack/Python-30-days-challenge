# Jiya Pal - Day 4: If-Else Statement
# IFTM University | Target: IAS 2030 🇮🇳

print("=== JIYA KA GRADE CHECKER ===")
marks = int(input("Apne marks daalo: "))

if marks >= 90:
    grade = "A+ | IAS Pakka 👑"
elif marks >= 75:
    grade = "A | Thodi mehnat aur 💪"
elif marks >= 60:
    grade = "B | Padh le Didi 💻"
else:
    grade = "C | Chappal ready hai 👡😂"

print("\nResult:", grade)

'''
=== SAMPLE OUTPUT ===
=== JIYA KA GRADE CHECKER ===
Apne marks daalo: 98

Result: A+ | IAS Pakka 👑
'''
