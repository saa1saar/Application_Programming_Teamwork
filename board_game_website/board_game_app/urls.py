#Defines URL patterns for board_game_app

from django.urls import path
from . import views

app_name = 'board_game_app'
urlpatterns = [
    #Homepage
    path('', views.index, name='index'),
    #Page that shows all the board games
    path('BoardGames/', views.BoardGames, name='BoardGames'),
    #Detail page for a single board game 
    path('BoardGame/<int:boardgame_id>/', views.boardgame, name='BoardGame'),
    #Page for adding a new board game
    path('new_boardgame/', views.new_boardgame, name='new_boardgame'),
]