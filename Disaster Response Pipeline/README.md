# Disaster Response Pipeline Project

### Table of Contents
+ <a href='#Project Summary'><h4>Project Summary</h4></a>
+ <a href='#Files Description'><h4>File Description</h4></a>
+ <a href='#Installation'><h4>Installation</h4></a>
+ <a href='#Instructions'><h4>Instructions</h4></a>
+ <a href='#License'><h4>License</h4></a>
+ <a href='#Acknowledgement'><h4>Acknowledgement</h4></a>

<h3>Project Summary</h3>
<a id='#Project Summary'></a>
This project was made avaialable as part projects for successful completion of Udacity Data Scientist Nanodegree to analyze disaster data from Figure Eight to build a model for an API that classifies disaster messages. The dataset contains labeled data and tweets, messages from real-life disasters using Natural Language Process (NLP) to perform necessary text preparation and using Machine Learning pipelines for the text classifications.

The project is divided in three different sections:
1. Extract, Transform and Load (ETL) : A Pipeline was developed to extract the data from the sources provided, perform necessary data cleaning and then load the clean data into a database for Machine Learning Processing

2. NLP /ML Pipelines development : This phase entail loading the data into an NLP pipeline to perform necessary text preprocessing and a Machine Learning Pipeline also developed to train the preprocessed data model to be able to properly classify the messages in the categories

3. Deployment : Model deployed in a Web App to show model results also to predict new messages in real-time

### Files Desription
<a id='#Files Desription'></a>
data
DisasterResponse.db: SQLlite database of combined message data and categories
disaster_categories.csv: Message category raw data
disaster_messages.csv: Message raw text
process_data: Python script for processing the raw data and generating the DisasterResponse.db
models
classifier.pkl: Saved message classification model
train_classifier.py: Python script for training the classifier model
app
templates: HTML templates folder
run.py: Python script for website generation

### Installation
<a id='#Installation'></a>
To be able to perform all the task stated above in the different phases, Python should be installed with the following libraries need;
Python version used 3.7
+ Scikit-learn
+ NLTK
+ Numpy
+ Pandas
+ SQLAlchemy
+ Flask 
+ Plotly

### Instructions
<a id='#Instructions'></a>
1. Run the following commands in the project's root directory to set up your database and model.
      + To run ETL pipeline that cleans data and stores in database `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
       _If a database is previously created then you should delete it first._
      + To run ML pipeline that trains classifier and saves `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app. `python run.py`

3. Go to http://localhost:3001/

### License
<a id='Licence'></a>
License: MIT

### Motivation
<a id='#Motivation'></a>
This project was made to help people in disasters situation to send there messages and easily to be classified by the meant organization.

### Acknowledgement
<a href=http://udacity.com>Udacity</a> For great course materials and <a href=https://appen.com/about-us/>Figure Eight </a> for their contributions in  making the dataset available to analyze and gather insights to solve problem.
