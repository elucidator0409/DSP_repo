from sentence_transformers import SentenceTransformer


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

if __name__ == "__main__":
    save_model("multi-qa-MiniLM-L6-cos-v1")