from flask import jsonify
from flask.views import MethodView

# Sample movie catalog data used to demonstrate the app's behavior.
movies = {
    "123": {"title": "City Lights", "description": "A thoughtful story about ambition and second chances."},
    "456": {"title": "Night Signal", "description": "A suspenseful thriller centered on a missing radio host."},
    "789": {"title": "River Echo", "description": "A reflective drama following a family reunion across generations."},
}


class Movies(MethodView):
    def get(self, movie_id):
        if movie_id is None:
            return jsonify({"movies": [dict({"title": movie["title"]}, **{"id": i}) for i, movie in movies.items()]})
        else:
            return jsonify({"movie": movies[str(movie_id)]})
