answers = ["a", "a", "a", "c"]
correct = ["a", "c", "d", "c"]

score = 0

for given, right in zip(answers, correct):
    if given == right:
        score += 1

print(f"Score: {score}/4")