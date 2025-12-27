from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import json

ROOT = Path(__file__).parent
TEMPLATES = ROOT / "app" / "templates"
OUT = ROOT / "dist"
OUT.mkdir(exist_ok=True)

env = Environment(loader=FileSystemLoader(str(TEMPLATES)))

data_path = ROOT / "data" / "profile.json"
p = json.loads(data_path.read_text(encoding="utf-8"))

def render_page(template_name: str, out_name: str, page_path: str):
    tpl = env.get_template(template_name)
    html = tpl.render(p=p, page_path=page_path)
    (OUT / out_name).write_text(html, encoding="utf-8")

render_page("index.html", "index.html", "/")

if (TEMPLATES / "projects.html").exists():
    render_page("projects.html", "projects.html", "/projects.html")

print("OK -> dist/")
