from flask import Flask, request, jsonify, render_template
import requests
import sqlite3

app = Flask(__name__)
API_KEY = "7585a4f9"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search')
def search_movie():
    title = request.args.get('title')
    if not title:
        return "Please enter a movie title", 400

    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        return render_template('result.html', movie=data)
    else:
        return "Movie not found", 404

if __name__ == '__main__':
    app.run(debug=True)
