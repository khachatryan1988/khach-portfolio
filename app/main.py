import json
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "profile.json"

app = FastAPI(title="Portfolio")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

def load_profile() -> dict:
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    p = load_profile()
    return templates.TemplateResponse("index.html", {"request": request, "p": p})

@app.get("/projects", response_class=HTMLResponse)
def projects(request: Request):
    p = load_profile()
    return templates.TemplateResponse("projects.html", {"request": request, "p": p})
