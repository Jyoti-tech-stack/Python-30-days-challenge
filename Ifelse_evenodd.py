# ========================================
# Day 4: Even Odd and Divisibility Check
# Author: Jiya Pal
# ========================================

num = int(input("Enter a number: "))

# Even or Odd
if num % 2 == 0:
    print(f"{num} is Even number")
else:
    print(f"{num} is Odd number")

# Divisible by 5
if num % 5 == 0:
    print(f"{num} is Divisible by 5")
else:
    print(f"{num} is Not Divisible by 5")

# Bada hai ya chota
if num > 100:
    print("Number is Bada")
else:
    print("Number is Chota")
