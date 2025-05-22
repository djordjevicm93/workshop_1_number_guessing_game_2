from flask import Flask, request, render_template

movies = {
    "favourite": ["A New Hope", "Empire Strikes Back", "Return of the Jedi",
                  "The Force Awakens", "Jaws", "Predator", "Mad Max",
                  "Back to the Future", "2001: A Space Odyssey", "Robocop",
                  "The Hitchhiker's Guide to the Galaxy", "Doctor Who",
                  "Aliens", "Alien", "Terminator", "Blade Runner", "Matrix"],

    "hated": ["The Phantom Menace", "Attack of the Clones", "Star Trek",
              "Alien Resurrection", "Twilight"]
}

app = Flask(__name__)
@app.route("/movies", methods = ["GET", "POST"])
def favourited_and_hated():
    if request.method == "GET":
        return render_template("form_movies.html")
    if request.method == "POST":
        title = request.form["title"]
        if title in movies["favourite"]:
            return "favourite"
        elif title in movies["hated"]:
            return "hated"
        else:
            return "no such movie"
        
if __name__ == "__main__":
    app.run(debug=True)
