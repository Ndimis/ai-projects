#!/usr/bin/env python3
import os
import json
import sys
from pathlib import Path

try:
    import yaml  # pip install pyyaml
except ImportError:
    print("pyyaml is required. pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(".")
README = ROOT / "README.md"
START = "<!-- PROJECT_TABLE_START -->"
END = "<!-- PROJECT_TABLE_END -->"

def load_meta(folder: Path):
    """Charge project.yaml ou project.json s'ils existent. Retourne None si absent/incomplet."""
    yml = folder / "project.yaml"
    jsn = folder / "project.json"
    data = None
    if yml.exists():
        data = yaml.safe_load(yml.read_text(encoding="utf-8"))
    elif jsn.exists():
        data = json.loads(jsn.read_text(encoding="utf-8"))
    if not data:
        return None
    # champs minimum
    required = {"name", "category", "description"}
    if not required.issubset(data.keys()):
        return None
    # lien relatif vers le dossier
    data["link"] = f"./{folder.name}"
    return {
        "category": str(data["category"]).strip(),
        "name": str(data["name"]).strip(),
        "description": str(data["description"]).strip(),
        "link": data["link"],
    }

def build_table(rows):
    header = [
        "| Category | Project Name | Description | Link |",
        "|---------|--------------|-------------|------|",
    ]
    body = []
    for r in rows:
        # Lien Markdown vers le dossier du projet
        link_md = f"[Open]( {r['link']} )".replace("  ", " ")
        body.append(f"| {r['category']} | {r['name']} | {r['description']} | {link_md} |")
    return "\n".join(header + body) + ("\n" if body else "")

def find_projects():
    rows = []
    for item in sorted(ROOT.iterdir()):
        if not item.is_dir():
            continue
        if item.name.startswith(".") or item.name in {".git", ".github"}:
            continue
        meta = load_meta(item)
        if meta:
            rows.append(meta)
    # tri par catégorie puis nom
    rows.sort(key=lambda x: (x["category"].lower(), x["name"].lower()))
    return rows

def update_readme(table_md: str):
    content = README.read_text(encoding="utf-8")

    # Si les balises n'existent pas, on les ajoute après le premier titre
    if START not in content or END not in content:
        insertion = f"{START}\n{table_md}{END}"
        if "\n## 📂 Project Index" in content:
            content = content.replace("## 📂 Project Index", "## 📂 Project Index\n\n" + insertion)
        else:
            # fallback : append à la fin
            content = content.rstrip() + "\n\n## 📂 Project Index\n\n" + insertion + "\n"
        README.write_text(content, encoding="utf-8")
        return True

    # Remplacement entre balises
    pre, _mid, post = content.partition(START)
    _mid2, _end, post_after = post.partition(END)
    new_content = f"{pre}{START}\n{table_md}{END}{post_after}"
    changed = new_content != content
    if changed:
        README.write_text(new_content, encoding="utf-8")
    return changed

def main():
    rows = find_projects()
    table_md = build_table(rows)
    changed = update_readme(table_md)
    if changed:
        print("README updated.")
    else:
        print("README already up-to-date.")

if __name__ == "__main__":
    main()