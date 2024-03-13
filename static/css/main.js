const searchActionMovies = async () => {
    const query = {
        "query": {
            "match": {
                "genre": "action"
            }
        }
    };

    try {
        const response = await fetch('http://your-elasticsearch-server:9200/movies/_search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(query)
        });

        if (!response.ok) {
            throw new Error('Failed to fetch movies');
        }

        const data = await response.json();
        return data.hits.hits.map(hit => hit._source);
    } catch (error) {
        console.error('Error fetching movies:', error);
        return [];
    }
};

// Example usage:
searchActionMovies().then(movies => {
    console.log('Action Movies:', movies);
    // Display the movies on your webpage
});
