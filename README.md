# 🧠 Sentimental Analysis

A lightweight Python program to detect the sentiment of a given sentence based on predefined emotion word sets.  
It can detect six sentiments: **Strongly Positive**, **Positive**, **Neutral**, **Negative**, **Strongly Negative**, and **Mixed Sentiment**.

---

## 💡 Features

- Detects and scores sentiment from user-input text.
- Handles:
  - ✅ Positive & Negative emotion words
  - 💪 Intensifiers (e.g., _really_, _super_, _totally_)
  - ❌ Negators (e.g., _not_, _never_, _none_)
  - 🔁 Contrast indicators (e.g., _but_, _however_, _although_)
  - 🙃 Sarcasm cues (e.g., _yeah right_, _sure_, _as if_)
  - ❗ Exclamations boost emphasis
- Supports **Mixed Sentiment** detection.
- Simple CLI interface.
- Pure Python — no external libraries required.

---

## 🧰 Built With

- 🐍 Python 3.x
- 🧩 Built-in `re` (Regex) module

---

## ▶️ How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/Poulabi8137/Micro_IT_Sentimental-Analysis_Project.git

2. **Run the script using Python**

   ```bash
   python sentiment_analyzer.py
3. **Use the analyzer in CLI**

   - Type your sentence and press Enter.
   - Get instant feedback on sentiment.
   - Type `exit` to quit.

---

## ⚙️ Sentiment Detection Logic

| **Sentiment**         | **Score Logic**                                               |
|-----------------------|---------------------------------------------------------------|
| Strongly Positive     | `score > 1.0`                                                  |
| Positive              | `0.2 < score ≤ 1.0`                                            |
| Neutral               | `-0.2 ≤ score ≤ 0.2`                                           |
| Mixed Sentiment       | Contains both strong positive and strong negative cues        |
| Negative              | `-1.0 ≤ score < -0.2`                                          |
| Strongly Negative     | `score < -1.0`                                                 |

- **Negations** flip the sentiment.
- **Sarcasm cues** can reverse or downplay the actual emotion.
- **Contrast words** like _but_, _however_ reduce sentiment strength.
- **Exclamation marks** add emphasis.
## 💬 Example

```bash
Enter sentence:
> I'm so happy, but honestly a bit nervous.

Analyzing: I'm so happy, but honestly a bit nervous.
Sentiment Detected: Mixed Sentiment
