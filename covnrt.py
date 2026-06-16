import json

filename = "Chunk.ipynb"

with open(filename, "r", encoding="utf-8") as f:
    nb = json.load(f)

if "widgets" in nb.get("metadata", {}):
    del nb["metadata"]["widgets"]

with open(filename, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)

print("Notebook repaired.")