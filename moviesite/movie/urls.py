from .views import *
from rest_framework import routers
from django.urls import  path, include

router = routers.SimpleRouter()
router.register(r'movie_languages', MovieLanguagesViewSet, basename='movie_languages_list'),
router.register(r'moments', MomentsViewSet, basename='moments_list'),
router.register(r'rating', RatingViewSet, basename='rating_list'),
router.register(r'favorite', FavoriteViewSet, basename='favorite_list'),
router.register(r'favorite_movie', FavoriteMovieViewSet, basename='favorite_movie_list'),
router.register(r'history', HistoryViewSet, basename='history_list'),

urlpatterns = [
    path('', include(router.urls)),
    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('users/', ProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', ProfileEditAPIView.as_view(), name='user_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('actor/', ActorListAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor_detail'),
    path('director/', DirectorListAPIView.as_view(), name='director_list'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]