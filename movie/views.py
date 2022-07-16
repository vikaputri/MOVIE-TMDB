from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
import requests
from datetime import datetime
from .models import Fav_Movie, Watchlist_Movie

api_key = "***"
movie_all = "https://api.themoviedb.org/3/trending/movie/day?api_key={api_key}&page={number}"
movie_id = "https://api.themoviedb.org/3/movie/{id}?api_key={api_key}"
video_id = "https://api.themoviedb.org/3/movie/{id}/videos?api_key={api_key}"
youtube_url = "https://youtube.com/embed/{video_key}"

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def home(request):
    result = []
    for x in range(1, 10):
        x+=1
        api = movie_all.format(api_key=api_key, number=str(x))
        data = requests.get(api).json()
        hasil = data['results']
        result.extend(hasil)
    paginator = Paginator(result, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'home.html', context)

def detail(request, id):
    get_movie_url = movie_id.format(api_key=api_key, id=id)
    movie_details = requests.get(get_movie_url).json()
    
    title = movie_details.get("title")
    poster = movie_details.get('poster_path')
    overview = movie_details.get('overview')
    status = movie_details.get("status")
    vote_average = movie_details.get("vote_average")
    tagline = movie_details.get("tagline")
    genres = []
    for genre in movie_details.get("genres"):
        genres.append(genre.get("name"))
    
    str_date = movie_details.get("release_date")
    if str_date:
        release_date = datetime.strptime(str_date, '%Y-%m-%d').date()
    else:
        release_date = ''
    
    get_video_url = video_id.format(id=id, api_key=api_key)
    videos = requests.get(get_video_url).json()
    movie_videos_list = videos['results']
    trailer = {}
    trailer_key, trailer_name, trailer_url = "", "", ""
    for trailer in movie_videos_list:
        if trailer['type'] == "Trailer":
            trailer_key = trailer['key']
            trailer_url = youtube_url.format(video_key=trailer_key)
            break

    fav_id=""
    watch_id=""
    if request.user.is_authenticated:
        if 'fav_id' in request.GET:
            movie_data = Fav_Movie(fav_id = id,
                                    title = title,
                                    vote_count = movie_details.get("vote_count"),
                                    poster_path = poster
                                )
            movie_data.save()
            fav_id = id
        if 'delete_fav_id' in request.GET:
            data = Fav_Movie.objects.filter(fav_id=fav_id)
            data.delete()
        if 'watch_id' in request.GET:
            movie_data = Watchlist_Movie(watch_id = id,
                                    title = title,
                                    vote_count = movie_details.get("vote_count"),
                                    poster_path = poster
                                )
            movie_data.save()
            watch_id=id
        if 'delete_Watchlist_id' in request.GET:
            data = _Movie.objects.filter(watch_id=watch_id)
            data.delete()
    
    context = {'title': title, 'poster': poster, 'overview': overview, 'genres': genres, 
        'vote_average':vote_average, 'status':status, 'tagline':tagline, 
        'release_date': release_date, 'movie_videos_list':movie_videos_list, 
        'trailer_url':trailer_url, 'fav_id':fav_id, 'watch_id':watch_id}

    return render(request, 'detail.html', context)

def watchlist(request):
    data = Watchlist_Movie.objects.all()
    context = {"data": data}
    return render(request, "watchlist.html", context)

def saved(request):
    data = Fav_Movie.objects.all()
    context = {"data": data}
    return render(request, "saved.html", context)