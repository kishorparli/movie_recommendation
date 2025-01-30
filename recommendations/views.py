from django.shortcuts import render
from .api_client import movie

def movie_list(request):
    popular_movies = movie.popular()
    movies = [
        {
            "title": m.title,
            "overview": m.overview,
            "poster_url": f"https://image.tmdb.org/t/p/w500{m.poster_path}",
            "release_date": m.release_date,
        }
        for m in popular_movies
    ]
    return render(request, "recommendations/movie_list.html", {"movies": movies})
