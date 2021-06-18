import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


filename = 'model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

class CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        try:
            return super().find_class(__name__, name)
        except AttributeError:
            return super().find_class(module, name)

vectorizer = CustomUnpickler(open('vectorizer.pickle', 'rb')).load()


def check_text(text):
    X_predict = vectorizer.transform([text])
    return loaded_model.predict(X_predict)

def predict_review(new_review):
  new_review = re.sub('[^a-zA-Z]', ' ', new_review)
  new_review = new_review.lower()
  new_review = new_review.split()
  ps = PorterStemmer()
  all_stopwords = stopwords.words('english')
  new_review = [ps.stem(word) for word in new_review if not word in set(all_stopwords)]
  new_review = ' '.join(new_review)
  new_corpus = [new_review]
  new_X_test = vectorizer.transform(new_corpus).toarray()
  new_y_pred = loaded_model.predict(new_X_test)
  return new_y_pred
print(predict_review('When you and your boys discover a hoe '))