IMDb Movie Search System with Elasticsearch
This project is a movie search system designed to search IMDb movie data using Elasticsearch.

Table of Contents
Overview
Features
Requirements
Setup
Usage


Overview
The IMDb Movie Search System allows users to search for movies by title, genre, director, year, or runtime. It utilizes Elasticsearch for efficient searching and indexing of IMDb movie data.

Features
Search for movies by title, genre, director, year, or runtime
Utilizes Elasticsearch for fast and accurate search results
Simple user interface using Tkinter
Requirements
Python 3.x
Elasticsearch
IMDb movie dataset (or any similar dataset)
Setup

Clone the repository:
git clone 'https://github.com/Anirudh5d/ElastiSearch---Movies-SearchEngine.git'
cd ElastiSearch---Movies-SearchEngine

Install dependencies:
pip install -r requirements.txt

Set up Elasticsearch:
Install Elasticsearch according to the instructions provided on the official Elasticsearch website.
Start Elasticsearch service.

Import IMDb movie dataset:
dataset link : https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows
Import the IMDb movie dataset into Elasticsearch. using the upload_imdb_movies_datat2ES.py

Run the application:
python app.py
Enter your movie search query in the provided search field.

Click the "Search" button to initiate the search.

View the search results displayed in the text area.



