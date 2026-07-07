# ========================================
# Day 4: If-Else with Numbers
# Author: Jiya Pal
# ========================================

# User se number lena
num = int(input("Enter a number: "))

# If-Else condition
if num > 0:
    print(f"{num} is Positive number")
elif num < 0:
    print(f"{num} is Negative number")
else:
    print("Number is Zero")

print("--------------------")

# Ek aur example: Pass/Fail
marks = int(input("Enter your marks: "))

if marks >= 33:
    print("Result: PASS")
else:
    print("Result: FAIL")
