import json
movie = {
    "title":"BDCC",
    "year": 2025,
    "actors": ["waw", "awa", "bawa"]
}
with open("movie.json" , "w") as file:
    json.dump(movie, file)

with open("movie.json", "r") as file:
    move_loaded=json.load(file)
    print(f"title: {move_loaded["title"]} year: {move_loaded["year"]} actord:{move_loaded["actors"]}")

    