import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("data.csv")
feedback = data["feedback"]

# Preprocess the text data
def preprocess_text(text):
  text = text.lower()
  text = text.replace("[^a-zA-Z0-9\s]", "")
  stopwords = ["the", "and", "is", "a", "of", "to", "in", "it", "you", "that", "on"]
  text = " ".join([word for word in text.split() if word not in stopwords])
  return text

feedback_preprocessed = [preprocess_text(text) for text in feedback]

# Calculate word frequency
word_counts = Counter(" ".join(feedback_preprocessed).split())

# Get user input for N
N = int(input("Enter the number of top words to display: "))

# Display top N most frequent words
top_words = word_counts.most_common(N)
print("\nTop", N, "most frequent words and their counts:")
for word, count in top_words:
  print(f"{word}: {count}")

# Plot the bar graph
plt.figure(figsize=(10, 6))
plt.bar([word for word, _ in top_words], [count for _, count in top_words])
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top N Most Frequent Words in Customer Feedback")
plt.show()

