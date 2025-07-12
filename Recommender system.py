import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


data = {
    'title': [
        'The Matrix', 'Inception', 'Interstellar', 'The Dark Knight', 'Avengers: Endgame'
    ],
    'genre': [
        'sci-fi action', 'sci-fi thriller', 'sci-fi drama', 'action crime', 'action superhero'
    ]
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(df['genre'])


similarity = cosine_similarity(genre_matrix)


def recommend(title):
    index = df[df['title'] == title].index[0]
    scores = list(enumerate(similarity[index]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    print(f"\nRecommendations for '{title}':")
    for i in sorted_scores[1:4]:  # Exclude the input itself
        print(f"- {df.iloc[i[0]]['title']} ({df.iloc[i[0]]['genre']})")


recommend("Inception")
