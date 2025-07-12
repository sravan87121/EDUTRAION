import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# 1. Sample dataset
data = {
    'title': [
        'The Matrix', 'Inception', 'Interstellar', 'The Dark Knight', 'Avengers: Endgame'
    ],
    'genre': [
        'sci-fi action', 'sci-fi thriller', 'sci-fi drama', 'action crime', 'action superhero'
    ]
}

df = pd.DataFrame(data)

# 2. Convert genre text into vectors
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(df['genre'])

# 3. Compute similarity between movies
similarity = cosine_similarity(genre_matrix)

# 4. Recommendation function
def recommend(title):
    index = df[df['title'] == title].index[0]
    scores = list(enumerate(similarity[index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    print(f"\nRecommendations for '{title}':")
    for i in sorted_scores[1:4]:  # Exclude the input itself
        print(f"- {df.iloc[i[0]]['title']} ({df.iloc[i[0]]['genre']})")

# 5. Test it
recommend("Inception")