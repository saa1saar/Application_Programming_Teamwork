#Defines URL patterns for board_game_app

from django.urls import path
from . import views
app_name = 'board_game_app'
urlpatterns = [
    #Homepage
    path('', views.index, name='index'),
    #Page that shows all the board games
    path('BoardGames/', views.BoardGames, name='Boardgames'),
    #Detail page for a single board game 
    path('BoardGames/<int:BoardGame_id>/', views.topic, name='BoardGame'),
]