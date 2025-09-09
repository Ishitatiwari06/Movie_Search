# 🎬 Movie Search App

A fast, interactive Movie Search Web Application built with FastAPI, Jinja2 templates, and the OMDb API.
Users can search for movies by title and see details including poster, genre, plot, and IMDb rating.

## 🚀 Features

🔍 Search movies by title

🎭 Display details: Title, Year, Genre, Plot, IMDb Rating

🖼️ Shows movie poster

⚠️ Handles invalid or missing movie names gracefully


## 🛠️ Tech Stack

Backend: FastAPI

Frontend: HTML, CSS (via Jinja2 templates)

API: OMDb API

Server: Uvicorn

## 📂 Project Structure
movie-search-app/
 ├── movieapp.py          # Main FastAPI application
 ├── requirements.txt     # Project dependencies
 └── templates/           # HTML templates
      ├── index.html      # Search page
      └── result.html     # Result page

## ⚡ Getting Started
1️⃣ Clone the Repository
git clone https://github.com/Ishitatiwari06/Movie_Search
cd movie-search-app

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Add Your OMDb API Key

Get a free key from OMDb API
.

Open movieapp.py and replace:

API_KEY = "your_api_key_here"

4️⃣ Run the Application
uvicorn movieapp:app --reload


Open your browser at 👉 http://127.0.0.1:8000

## ✨ Future Improvements

Add Bootstrap or Tailwind CSS for modern UI

Show related movies / multiple results

Add user authentication (login/signup)

## 🤝 Contributing

Contributions are welcome!

Fork the repo

Create a new branch (feature-branch)

Commit your changes

Open a Pull Request 🚀

## 📜 License

This project is licensed under the MIT License.

MIT License

Copyright (c) 2025 Ishita Tiwari

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
