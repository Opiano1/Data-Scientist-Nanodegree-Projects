#Importing important Libraries needed for the Text Preprocessing and Modelling
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
import nltk
import re
nltk.download(['punkt', 'wordnet','stopwords'])
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from sqlalchemy import create_engine
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,f1_score,precision_recall_curve,accuracy_score
import numpy as np
from sklearn.multioutput import MultiOutputClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, GridSearchCV
import joblib
import pickle

import sys


def load_data(database_filepath):
    """
    The cleaned data in the database is loaded into a dataframe
    to perform initial machine learning process.
    
    Args:
        database_filepath : The path of the database that contain
        the clean data data to be loaded into the dataframe
    
    Returns:
           The dataset is separated into target Y and explanatory features
           X
    """
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql('df', engine)
    # extract values from X and y
    X =  df['message'].values
    Y = df.iloc[:, 4:].values
    category_names = list(df.columns[4:])
    return X, Y, category_names

def tokenize(text):
    """
    The explanatory feature X is preprocessed and a tokenized
    feature will be generated
    
    Args:
        text: Message data for tokenization.
        
    Return:
        clean_tokens: Result list after tokenization.
    """
    text = re.sub(r'[^A-Za-z0-9]'," ",text.lower())
    text = word_tokenize(text)
    words = [w.strip() for w in text if w not in stopwords.words("english")]
    lemmatizer = WordNetLemmatizer()
    clean_tokens = [WordNetLemmatizer().lemmatize(w) for w in words]
    
    return clean_tokens

def build_model():
    
    """
    A pipeline model with a cross validated hyper-parameters to be used to fit
    the training set is developed
    
    Args: None
    
    Return:
           cv: Cross validated pipeline model to fit the training dataset
    """
    pipeline = Pipeline([('CountVect',CountVectorizer(tokenizer=tokenize)),
                     ('Tfidf',TfidfTransformer()),
                     ('MultiClass',MultiOutputClassifier(OneVsRestClassifier(LinearSVC())))])
    
    
    parameters = {'CountVect__binary': [False,True],
              'Tfidf__norm': ['l1','l2'],
             'MultiClass__estimator__estimator__C': [1.0,3.0,5.0]
             }

    cv = GridSearchCV(pipeline,param_grid=parameters)
    return cv
    

def evaluate_model(model, X_test, Y_test, category_names):
    """
    The performance of the model is evaluated on the test datasets
    using evaluation metrics of accuracy score
    
    Args:
        model: Pipeline model with a cross validated features to train
               the data
        
        X_test : The test dataset to make prediction on using the
                trained data
        
        Y_test : The true value to evaluate the predicted value
                of the model
        
        Category_names : Column names of all features
        
     
    Returns:
            None , however the evaluation of the model is displayed
    """
    Y_pred = model.predict(X_test)
    print('---------------------------------')
    for i in range(Y_test.shape[1]):
        print('{} accuracy {}'.format(category_names[i],accuracy_score(Y_test[:,i],Y_pred[:,i])))

def save_model(model, model_filepath):
    """
    The model developed in saved as a pickle file 
    to be used for future data in another platform
    
    Args:
        model: Pipeline model with a cross validated features to train
               the data
        
        model_filepath: Where the pickled model should be saved
        
    Return:
           None
    """
    
    joblib.dump(model, model_filepath)
    

def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()