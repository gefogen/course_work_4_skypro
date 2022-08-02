from project.dao import MovieDAO, DirectorDAO, GenreDAO, UserDAO, FavouriteDAO
from project.dao.models import Movie, Genre, Director, User, Favourite
from project.services import MovieService
from project.services import DirectorService
from project.services import GenreService
from project.services import UserService
from project.services import AuthService
from project.services import FavouriteService
from project.setup_db import db

### MOVIE ###
movie_dao = MovieDAO(session=db.session, model=Movie)
movie_service = MovieService(dao=movie_dao)

### GENRE ###
genre_dao = GenreDAO(session=db.session, model=Genre)
genre_service = GenreService(dao=genre_dao)

### DIRECTOR ###
director_dao = DirectorDAO(session=db.session, model=Director)
director_service = DirectorService(dao=director_dao)

### USER ###
user_dao = UserDAO(session=db.session, model=User)
user_service = UserService(dao=user_dao)

### AUTH ###
auth_service = AuthService(user_service=user_service)

### FAVOURITE ###
favourite_dao = FavouriteDAO(session=db.session, model=Favourite)
favourite_service = FavouriteService(dao=favourite_dao)