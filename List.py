# ========================================
# Day 24: Python List Basics
# Author: Jiya Pal
# Btech AI/ML 1st Year - 30 Day Journey
# ========================================

print("=== LIST IN PYTHON ===")

# 1. List banana
fruits = ["Apple", "Banana", "Mango", "Grapes"]
print("Meri List:", fruits)

# 2. List ki cheez nikalna - index 0 se shuru hota hai
print("Pehla fruit:", fruits[0])
print("Teesra fruit:", fruits[2])

# 3. List me naya item add karna
fruits.append("Orange")
print("Add karne ke baad:", fruits)

# 4. List me item badalna
fruits[1] = "Strawberry"
print("Badalne ke baad:", fruits)

# 5. List ki length
print("Total items:", len(fruits))

# 6. Loop se sab print karna
print("\nSabhi fruits ek ek karke:")
for fruit in fruits:
    print("-", fruit)
