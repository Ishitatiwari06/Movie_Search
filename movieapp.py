from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

API_KEY = "7585a4f9"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, title: str):
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    response = requests.get(url).json()

    if response.get("Response") == "True":
        return templates.TemplateResponse("result.html", {
            "request": request,
            "movie": response
        })
    else:
        return templates.TemplateResponse("result.html", {
            "request": request,
            "error": "❌ Movie not found. Try another title!"
        })
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("movieapp:app", host="127.0.0.1", port=8000, reload=True)
