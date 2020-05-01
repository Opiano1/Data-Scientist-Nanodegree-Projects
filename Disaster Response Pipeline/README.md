
# Disaster Response Pipeline Project
### Table of Contents
Description
Dependencies
Installing
Instructions
License
Acknowledgement
Description
This project is part of my data science nano degree program by Udacity in collaboration with figure eight. The dataset contains labeled data and tweets, messages from real-life disasters. the aim of this project is to build a tool that categorize messages using NLP (Natural Language Processing)

The project is divided in three different sections:

Data Processing, ETL pipeline to extract data from sources and to clean it finally save it in sqlite database
Machine Learning Pipeline to train model to be able to classify messages in categories
Web App to show model results also to predict new messages in real-time
Dependencies
Python libraries needed
Python version used 3.7
Machine Learning libraries Scikit-learn, Numpy, Pandas, SciPy
SQLAlchemy
Flask, Plotly
Installing:
Clone this GIT repository:

https://github.com/amrhwanis22/DisasterResponse.git

Instructions:
Run the following commands in the project's root directory to set up your database and model.

To run ETL pipeline that cleans data and stores in database python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db

If a database is previously created then you should delete it first.
To run ML pipeline that trains classifier and saves python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl

Run the following command in the app's directory to run your web app. python run.py

Go to http://localhost:3001/

License:
License: MIT

Motivation:
This project was made to help people in disasters situation to send there messages and easily to be classified by the meant organization.
Acknowledgement:
Udacity For great course materials

Figure Eight For the effort made to collect the dataset
