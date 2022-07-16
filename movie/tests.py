from django.test import TestCase
from .models import Fav_Movie, Watchlist_Movie
from django.urls import reverse
from django.contrib import admin
from django.apps import apps

class TestAdmin(TestCase):
    def test_all_models_are_registered(self):
        models = apps.get_models()

        for model in models:
            self.assertIs(True, admin.site.is_registered(model),
                    msg=f'Did you forget to register the "{model.__name__}" in the django-admin?')

class Fav_MovieTest(TestCase):
    def create_favmovie(
            self,
            fav_id= 921353,
            title = 'Wrong Place',
            vote_count = 1, 
            poster_path = 'https://image.tmdb.org/t/p/w500//9mxNku6g2JmGmKTGGEOpU4lvVWM.jpg'
        ):
        
        return Fav_Movie.objects.create(
            fav_id= fav_id,
            title = title,
            vote_count = vote_count, 
            poster_path = vote_count
        )

    def test_favmovie_creation(self):
        w = self.create_favmovie()
        self.assertTrue(isinstance(w, Fav_Movie))
        self.assertEqual(w.__str__(), w.title)
    
    def test_favmovie_list_view(self):
        w = self.create_favmovie()
        url = reverse("saved")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
    

class Watchlist_MovieTest(TestCase):
    def create_watchlistmovie(
            self,
            watch_id= 921353,
            title = 'Wrong Place',
            vote_count = 1, 
            poster_path = 'https://image.tmdb.org/t/p/w500//9mxNku6g2JmGmKTGGEOpU4lvVWM.jpg'
        ):
        
        return Watchlist_Movie.objects.create(
            watch_id= watch_id,
            title = title,
            vote_count = vote_count, 
            poster_path = vote_count
        )

    def test_watchlistmovie_creation(self):
        w = self.create_watchlistmovie()
        self.assertTrue(isinstance(w, Watchlist_Movie))
        self.assertEqual(w.__str__(), w.title)
    
    def test_watchlistmovie_view(self):
        w = self.create_watchlistmovie()
        url = reverse("watchlist")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)


