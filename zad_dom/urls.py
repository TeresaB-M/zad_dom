from django.contrib import admin
from django.urls import path
from z_d.views import MoviesView, SearchMoviesView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('movies/', MoviesView.as_view(), name='movies'),
    path("search_movie/", SearchMoviesView.as_view(), name='search_movies'),
]
