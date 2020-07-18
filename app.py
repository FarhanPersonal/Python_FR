import json
from pathlib import Path
 
movies = [{ "id": 1, "title": "Terminator", "year": 1984}, { "id": 2, "title": "Kindergarten", "year": 1990}]

data = json.dumps(movies)

Path("movies.json").write_text(data)