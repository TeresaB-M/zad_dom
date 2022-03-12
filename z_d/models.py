from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.name}'

class Movie(models.Model):
    title = models.CharField(max_length=128)
    director = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_director')
    screenplay = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_screenplay')
    starring = models.ManyToManyField(Person)
    year = models.IntegerField()
    rating = models.FloatField()
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f'{self.title}, {self.director}'
