def calculate_stipend(days, rate):
    total = days * rate
    return total

def predict_lpa(years_experience):
    base = 0
    growth_per_year = 12
    return base + (years_experience * growth_per_year)

def jiya_motivation():
    return "IFTM se Google tak. Code by code."

name = "Jiya"
month_stipend = calculate_stipend(30, 1500)
lpa_2026 = predict_lpa(0)  # 1st year = 0 exp
lpa_2030 = predict_lpa(4)  # 4th year end = 4 exp

print(f"Name: {name}")
print(f"Day 10 Stipend: ₹{month_stipend}")
print(f"2026 Target LPA: {lpa_2026}")
print(f"2030 Target LPA: {lpa_2030}")
print(jiya_motivation())
print("Day 10 Done: Functions unlocked. Google loading... 🚀")
