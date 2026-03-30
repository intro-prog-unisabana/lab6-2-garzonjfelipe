scores = []
scores = {}

while True:
    entry = input("Enter player and score as 'name score' (or type 'stop' to finish): ")

    if entry.lower() == "stop":
        break

    name, score = entry.split()
    score = int(score)

    if name in scores:
        scores[name] += score
    else:
        scores[name] = score

if len(scores) == 0:
    print("No scores recorded.")
else:
    top = max(scores, key=scores.get)
    print(f"Top scorer: {top} with {scores[top]} points.")