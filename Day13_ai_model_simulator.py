import random

def train_model(epochs):
    accuracy = 0
    print("=== Training Jiya's AI Model ===")
    for epoch in range(1, epochs + 1):
        accuracy += random.randint(5, 15)
        if accuracy > 95:
            accuracy = 95
        print(f"Epoch {epoch}/{epochs} - Accuracy: {accuracy}%")
    return accuracy

def predict_lpa(skills_count, projects):
    base_lpa = 3
    skill_boost = skills_count * 2
    project_boost = projects * 5
    return base_lpa + skill_boost + project_boost

def save_model_data(name, accuracy, lpa):
    with open("jiya_model.txt", "w") as file:
        file.write(f"Model Owner: {name}\n")
        file.write(f"Model Accuracy: {accuracy}%\n")
        file.write(f"Predicted LPA: {lpa}\n")
        file.write("Status: Google Ready 🚀\n")

name = "Jiya - BTech AI IFTM"
final_accuracy = train_model(5)
predicted_lpa = predict_lpa(13, 5)

print(f"\nFinal Model Accuracy: {final_accuracy}%")
print(f"Jiya's Predicted LPA: {predicted_lpa} LPA")
print("Day 13 Done: File Handling + AI Simulation ✅")

save_model_data(name, final_accuracy, predicted_lpa)
print("Model saved to jiya_model.txt")
