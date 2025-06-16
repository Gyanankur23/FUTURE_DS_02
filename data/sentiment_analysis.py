
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the reviews from the CSV file
df = pd.read_csv("sample_reviews.csv")

# Step 2: Define positive and negative keywords
positive_words = ["excellent", "amazing", "best", "recommend", "outstanding", "happy", "useful", "love", "great", "perfect", "fantastic"]
negative_words = ["not", "poor", "disappointing", "terrible", "damaged", "low", "pathetic", "misleading", "delayed", "worst"]

# Step 3: Check for positive or negative words in each review
df["is_positive"] = df["review"].str.contains("|".join(positive_words), case=False)
df["is_negative"] = df["review"].str.contains("|".join(negative_words), case=False)

# Step 4: Count the results
total_reviews = len(df)
positive_count = df["is_positive"].sum()
negative_count = df["is_negative"].sum()
neutral_count = total_reviews - (positive_count + negative_count)

# Step 5: Print the percentages
print("Positive Reviews:", positive_count, f"({positive_count / total_reviews * 100:.2f}%)")
print("Negative Reviews:", negative_count, f"({negative_count / total_reviews * 100:.2f}%)")
print("Neutral Reviews:", neutral_count, f"({neutral_count / total_reviews * 100:.2f}%)")

# Step 6: Show pie chart
labels = ["Positive", "Negative", "Neutral"]
sizes = [positive_count, negative_count, neutral_count]
colors = ["skyblue", "lightcoral", "lightgreen"]

plt.pie(sizes, labels=labels, colors=colors, autopct="%.2f%%", startangle=90)
plt.title("Sentiment Analysis of E-commerce Reviews")
plt.axis("equal")
plt.show()
