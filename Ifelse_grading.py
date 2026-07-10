# ========================================
# Day 4: Grading System using If-Elif-Else
# Author: Jiya Pal
# ========================================

marks = int(input("Enter your marks out of 100: "))

if marks >= 90:
    print("Grade: A+ 🔥")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 33:
    print("Grade: D - Pass")
else:
    print("Grade: F - Fail 😢")

print("Thank you!")
