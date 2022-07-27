from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import pandas as pd

def recommend(movie_id, dataset, cosine_matrix):
    '''
    Recommend movies with similar scripts
    '''
    recommendations = []

    index = dataset[dataset["id"] == movie_id].index[0]
    score_series = pd.Series(cosine_matrix[index]).sort_values(ascending = False)
    top_10_indices = list(score_series.iloc[1:11].index)

    for i in top_10_indices:
        recommendations.append(dataset["id"][i])

    return recommendations

def recommend_based_on_query(sentence_transformer, dataset, text_embeddings, query):
    '''
    Recommend movies based on user's query
    '''
    recommendations = []
    
    sentence_transformer = SentenceTransformer("multi-qa-MiniLM-L6-cos-v1")
    query = sentence_transformer.encode(query).reshape(1, -1)
    
    # Calculate consine similarity with text embeddings
    similarities = cosine_similarity(text_embeddings, query).reshape(-1)
    score_series = pd.Series(similarities).sort_values(ascending = False)
    top_10_indices = list(score_series.iloc[1:11].index)
    
    return dataset["id"][top_10_indices].tolist()