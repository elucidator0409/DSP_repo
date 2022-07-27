import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import pandas as pd
import json

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
    
    query = sentence_transformer.encode(query).reshape(1, -1)
    
    # Calculate consine similarity with text embeddings
    similarities = cosine_similarity(text_embeddings, query).reshape(-1)
    score_series = pd.Series(similarities).sort_values(ascending = False)
    top_10_indices = list(score_series.iloc[1:11].index)
    
    for i in top_10_indices:
        recommendations.append(dataset["id"][i])

    return recommendations

def save_model(model_name):
    '''
    Save model to the model folder
    '''
    model = SentenceTransformer(model_name)
    model.save("./model")

def load_model(model_path):
    '''
    Load model from the model folder
    '''
    return SentenceTransformer(model_path)

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

def lambda_handler(event, content):
    '''
    A simple lambda handler
    '''
    # Load the model
    transformer = load_model("./model")

    # Load text embedding
    text_embeddings = np.load("./embeddings/embeddings")

    # Load dataset
    dataset = pd.read_csv("./dataset/summary.csv")

    '''
    Get the query from event
    '''
    query = event["queryStringParameters"]["query"]

    # Convert into http response and send back
    result = recommend_based_on_query(transformer, dataset, text_embeddings, query)
    response = {
        "ids": result
    }

    # Get the related id
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response, cls=NpEncoder)
    }