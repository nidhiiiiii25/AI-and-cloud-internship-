from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: Sample movie reviews
reviews = [
    "I love this movie",
    "This film is amazing",
    "I hate this movie",
    "This movie is terrible",
    "The movie was okay"
]

# Step 2: Labels (sentiment)
# 1 = Positive, 0 = Negative
labels = [1, 1, 0, 0, 1]

# Step 3: Convert text to TF-IDF features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(reviews)

# Step 4: Train model
model = MultinomialNB()
model.fit(X, labels)

# Step 5: Test on new reviews
test_reviews = [
    "I love this film",
    "This is bad",
    "Amazing movie",
    "Worst film ever",
    "It was okay"
]

# Convert test data
X_test = vectorizer.transform(test_reviews)

# Predict
predictions = model.predict(X_test)

# Step 6: Show results
for review, pred in zip(test_reviews, predictions):
    sentiment = "Positive" if pred == 1 else "Negative"
    print(f"{review} --> {sentiment}")