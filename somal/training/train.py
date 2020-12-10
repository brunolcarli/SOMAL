import pickle
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np


def train_models():
    with open('somal/training/corpus.txt', 'r') as f:
        data = []
        lines = [line.strip() for line in f.readlines()[6:]]

        for line in lines:
            if line:
                try:
                    date = line.split('[')[1].split()[0]
                except:
                    continue
                try:
                    user = line.split(']')[1].split(':')[0].strip()
                except:
                    continue
                
                try:
                    message = line.split(':')[3].strip()
                except:
                    continue
                data.append((date, user, message))

    name_dict = {}
    date_dict = {}
    for log in data:
        # por nomefrom sklearn.pipeline import Pipeline
        if log[1] in name_dict.keys():
            name_dict[log[1]].append(log[2])
        else:
            name_dict[log[1]] = [log[2]]

        # por data
        if log[0] in date_dict.keys():
            date_dict[log[0]].append(log[2])
        else:
            date_dict[log[0]] = [log[2]]

    by = ['bruno' for _ in range(450)]
    ky = ['kamal' for _ in range(450)]

    X = []
    bruno = name_dict['Beelzebruno']
    for text in bruno:
        if len(X) == 450:
            break
        if 'sticker' in text:
            continue
        if 'image' in text:
            continue
        
        X.append(text)

    kamal = name_dict['Kamal Curi']
    for text in kamal:
        if len(X) == 900:
            break

        if 'sticker' in text:
            continue
        if 'image' in text:
            continue
        
        X.append(text)

    
    text_clf = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', MultinomialNB()),
    ])
    text_clf.fit(X, by+ky)
    predicted = text_clf.predict(X)
    print(np.mean(predicted == by+ky))

    with open('somal/training/bk_model', 'wb') as fpath:
        pickle.dump(text_clf, fpath)
