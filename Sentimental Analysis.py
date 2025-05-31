import re
def mood_check(text):
    print(f"\nAnalyzing: {text}")
    text = text.strip().lower()
    bits = re.findall(r'\b\w+\b', text)
    plus = {
        "admiration", "affection", "amusement", "awe", "calm", "compassion", "confidence", "contentment",
        "delight", "ecstasy", "empathy", "euphoria", "excitement", "forgiveness", "glee", "gratitude",
        "happiness", "hope", "interest", "joy", "love", "lust", "passion", "pride", "relief", "satisfaction",
        "serenity", "surprise", "sympathy", "tenderness", "trust", "wonder", "zeal"
    }
    minus = {
        "agony", "anger", "annoyance", "anxiety", "apathy", "boredom", "contempt", "defeat", "depression",
        "despair", "disappointment", "disgust", "dread", "embarrassment", "envy", "fear", "frustration",
        "guilt", "hatred", "horror", "hurt", "jealousy", "loneliness", "melancholy", "panic", "rage",
        "regret", "remorse", "sadness", "scorn", "shame", "shock", "sorrow", "worry"
    }
    punch = {"very", "extremely", "so", "really", "absolutely", "totally", "super"}
    flip = {"not", "no", "never", "none", "hardly"}
    twist = {"but", "however", "although", "though"}
    dry = {"yeah right", "sure", "as if", "obviously", "totally helpful", "real nice"}
    score = 0
    turned = False
    dry_flag = False
    for phrase in dry:
        if phrase in text:
            dry_flag = True
    for w in bits:
        if w in punch:
            score += 0.5
        elif w in flip:
            turned = True
        elif w in plus:
            score += 1
        elif w in minus:
            score -= 1
        elif w in twist:
            score *= 0.6
    if turned:
        score *= -1

    if dry_flag:
        if score > 0.2:
            score = -abs(score * 1.2)
        elif -0.2 <= score <= 0.2:
            score = -0.5

    if "!" in text:
        score += 0.5

    if score > 1.0:
        mood = "Strongly Positive"
    elif score > 0.2:
        mood = "Positive"
    elif -0.2 <= score <= 0.2:
        mood = "Neutral"
    elif score < -1.0:
        mood = "Strongly Negative"
    else:
        mood = "Negative"

    return mood

if __name__ == "__main__":
    print("Sentiment Analyzer: Type your sentence below (type 'exit' to quit)")
    while True:
        line = input("\nEnter sentence:\n> ")
        if line.strip().lower() == "exit":
            print("Exiting. Stay innovative!")
            break
        mood = mood_check(line)
        print(f"Sentiment Detected: {mood}")
