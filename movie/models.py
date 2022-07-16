from django.db import models

class Fav_Movie(models.Model):
    fav_id= models.CharField(max_length=50, blank = True, null = True)
    title = models.CharField(max_length=50, blank = True, null = True)
    vote_count = models.CharField(max_length=10, blank = True, null = True)
    poster_path = models.CharField( max_length=50, blank = True, null = True)

    def __str__(self):
        return self.title

class Watchlist_Movie(models.Model):
    watch_id= models.CharField(max_length=50, blank = True, null = True)
    title = models.CharField(max_length=50, blank = True, null = True)
    vote_count = models.CharField(max_length=10, blank = True, null = True)
    poster_path = models.CharField( max_length=50, blank = True, null = True)

    def __str__(self):
        return self.title