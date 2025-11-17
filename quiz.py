print("Eminem Quiz!!!")
print("....")
quiz = {
    "what was the most iconic eminem song of all time?": "The real slim shady",
    "what was eminem's most popular song on spotify?": "without me",
    "what was the best eminem album of all time?" : "marshall mathers LP",
    "what was the best colaboration song that eminem done ?" : "love the way you lie",
    "what was eminems band that he was in ?" : "D12",
}

score = 0

for question, correct_answer in quiz.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == correct_answer.lower():
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect. The correct answer is: {correct_answer}")

print(f"\nYour final score: {score}/{len(quiz)}")