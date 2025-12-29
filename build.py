from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import json
import shutil

ROOT = Path(__file__).parent
TEMPLATES = ROOT / "app" / "templates"
STATIC_SRC = ROOT / "app" / "static"
DATA = ROOT / "data" / "profile.json"
OUT = ROOT / "dist"

OUT.mkdir(exist_ok=True)

env = Environment(loader=FileSystemLoader(str(TEMPLATES)))

p = json.loads(DATA.read_text(encoding="utf-8"))

def render_page(template_name: str, out_name: str, page_path: str):
    tpl = env.get_template(template_name)
    html = tpl.render(p=p, page_path=page_path)
    (OUT / out_name).write_text(html, encoding="utf-8")

render_page("index.html", "index.html", "/")
if (TEMPLATES / "projects.html").exists():
    render_page("projects.html", "projects.html", "/projects.html")

# copy static -> dist/static
dst = OUT / "static"
if dst.exists():
    shutil.rmtree(dst)
if STATIC_SRC.exists():
    shutil.copytree(STATIC_SRC, dst)

print("OK -> dist: index.html, projects.html, static/")
