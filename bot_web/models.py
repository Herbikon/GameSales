from django.db import models

class Genre(models.Model):
    Genre_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Genre_name

class Developer(models.Model):
    Developers_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Developers_name

class Publisher(models.Model):
    Publishers_name = models.CharField(max_length=100, unique=True)  

    def __str__(self):
        return self.Publishers_name

class Tags(models.Model):
    Tag_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Tag_name

class Localization(models.Model):
    Voice = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Voice

class Games(models.Model):
    Name_game = models.CharField(max_length=200, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    localization = models.ForeignKey(Localization, on_delete=models.CASCADE)  

def __str__(self):
    return self.Name_game
