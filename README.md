# MOVIE-TMDB

## Description
A watch-list app built with Django using the TMDB (The Movie Database) API. This app can be access with link https://movie-tmdb-py.herokuapp.com/

## How to run on local machine
* Create Folder
```
mkdir movie
cd movie

```
* Clone Repository
```
git clone https://github.com/vikaputri/MOVIE-TMDB.git

```
* Create a Python virtualenv 
```
virtualenv -p python3 venv
source venv/bin/activate 
```
or
```
python3 -m venv env
venv/Scripts/Activate
```
* Change Directory
```
cd movie_tmdb
```
* Install dependencies
```
pip install -r requirements.txt
```
* Make changes to the schema in the models.py 
```
python manage.py migrate
```
* Run the Server
```
python manage.py runserver
```
* Open browser and view the app by opening the link http://127.0.0.1:8000/


## Technologies Used
* Python
* Django
* HTML
* CSS
* Bootstrap
* SQlite
