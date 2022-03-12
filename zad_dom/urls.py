from django.contrib import admin
from django.urls import path
from z_d.views import MoviesView, SearchMoviesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', MoviesView.as_view()),
    path("search_movie/", SearchMoviesView.as_view()),
]
