#Defines URL patterns for board_game_app

from django.urls import path
from . import views
app_name = 'board_game_app'
urlpatterns = [
    #Homepage
    path('', views.index, name='index'),
    #Page that shows all the Board Games
    path('BoardGames/', views.BoardGames, name='Boardgames'),
]