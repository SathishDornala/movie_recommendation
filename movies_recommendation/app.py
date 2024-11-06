from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load your recommendation data
df_result = pd.read_csv('MovieRecommendations.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form['movie_name']
    list_result = df_result[df_result['title'] == movie_name]
    
    if list_result.empty:
        recommendations = "No recommendations found."
    else:
        recommendations = list_result[['FirstMovieRecommendation', 'SecondMovieRecommendation', 'ThirdMovieRecommendation', 'FourthMovieRecommendation']].values.flatten().tolist()
    
    return render_template('index.html', recommendations=recommendations, movie_name=movie_name)

if __name__ == '__main__':
    app.run(debug=True)
