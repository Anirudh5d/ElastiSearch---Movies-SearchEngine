from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

app = Flask(__name__)

es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])
index_name = 'movie_&_tvshows_data'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    search_q = {
            "query": {
                "multi_match": {
                    "query": query,   
                    "type": "cross_fields",       
                    "fields": ["movie_name", "genre"]  
                }
            },
            'size': 25
        }
    search_results = es.search(index=index_name, body=search_q)
    unique_movies = set()
    movies = []
    for hit in search_results['hits']['hits']:
        movie_name = hit['_source']['movie_name']
        if movie_name not in unique_movies:
            movies.append(hit['_source'])
            unique_movies.add(movie_name)
    return render_template('search_results.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
