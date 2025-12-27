from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import json
import shutil

ROOT = Path(__file__).parent
TEMPLATES = ROOT / "app" / "templates"
STATIC = ROOT / "app" / "static"
DATA = ROOT / "data" / "profile.json"   # у тебя так в дереве
OUT = ROOT / "dist"

OUT.mkdir(exist_ok=True)

env = Environment(loader=FileSystemLoader(str(TEMPLATES)))

p = json.loads(DATA.read_text(encoding="utf-8"))

pages = [
    ("index.html", "/"),
    ("projects.html", "/projects.html"),
]

for tpl_name, path in pages:
    tpl = env.get_template(tpl_name)
    html = tpl.render(p=p, path=path)
    (OUT / tpl_name).write_text(html, encoding="utf-8")

# копируем статику в dist/static
dst_static = OUT / "static"
if dst_static.exists():
    shutil.rmtree(dst_static)
shutil.copytree(STATIC, dst_static)

print("OK -> dist готов:", [x[0] for x in pages], "+ static/")
