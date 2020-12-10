import pickle

def load_model(fpath):
    """
    Loads a trained machine learning model.
    param : fpath: <str> : file path to the model
    """
    with open(fpath, 'rb') as trained_model:
        model = pickle.load(trained_model)

    return model
