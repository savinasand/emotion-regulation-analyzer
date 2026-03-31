from textblob import TextBlob

def analyze_emotion(text):
    blob = TextBlob(text)
    
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # Tone
    if polarity > 0:
        tone = "Positive"
    elif polarity < 0:
        tone = "Negative"
    else:
        tone = "Neutral"

    # Intensity
    if abs(polarity) > 0.6:
        intensity = "High"
    elif abs(polarity) > 0.3:
        intensity = "Medium"
    else:
        intensity = "Low"

    # Regulation score (0-10)
    regulation_score = round((1 - abs(polarity)) * 10, 2)

    # Empathy
    empathy_words = ["understand", "feel", "sorry", "appreciate"]
    empathy = any(word in text.lower() for word in empathy_words)

    return {
        "Tone": tone,
        "Intensity": intensity,
        "Regulation Score (0-10)": regulation_score,
        "Empathy Detected": empathy
    }

# Ask for input
text = input("Enter a sentence: ")
result = analyze_emotion(text)

for key, value in result.items():
    print(f"{key}: {value}")
