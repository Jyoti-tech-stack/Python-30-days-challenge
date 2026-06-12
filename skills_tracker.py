def print_skill_progress(skill_list):
    print("Jiya's Skill Stack 2026:")
    for i in range(len(skill_list)):
        day = (i + 1) * 3
        print(f"Day {day}: {skill_list[i]} ✅")

def total_skills(skills):
    return len(skills)

name = "Jiya"
my_skills = ["Python Basics", "if-else", "Loops", "Functions", "Lists"]
total = total_skills(my_skills)

print_skill_progress(my_skills)
print(f"\nTotal Skills Learned: {total}/30")
print(f"{name} is {total * 3.33}% closer to Google 🚀")
print("Day 11 Done: Lists mastered. Resume building started.")
