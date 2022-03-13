from django.contrib import admin
from django.urls import path
from z_d.views import MoviesView, SearchMoviesView, DeleteMovie, DeletePerson

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('movies/', MoviesView.as_view(), name='films'),
    path('search_movie/', SearchMoviesView.as_view(), name='search_movies'),
    path('del-movie/{id_movie}/', DeleteMovie.as_view(), name='delete_movie'),
    path('del-person/{id}/', DeletePerson.as_view(), name='delete_movie'),
]
