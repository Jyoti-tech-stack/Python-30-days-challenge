# Day 25: For Loop with List - Jiya's 30 Day Python Challenge

print("=== DAY 25: FOR LOOP + LIST ===")

# 1. List banayi
skills = ["Python", "AI/ML", "GitHub", "Data Analysis"]

print("Mere Skills:")
# 2. For loop se ek karke print kiya
for skill in skills:
    print(f"- {skill} 🔥")

print("\n")

# 3. Numbers wali list
numbers = [10, 20, 30, 40, 50]
total = 0

print("Numbers aur unka double:")
for num in numbers:
    double = num * 2
    total = total + num
    print(f"{num} ka double = {double}")

print(f"\nTotal sum = {total}")

print("\nStatus: Future AI Engineer in Progress 💪")
