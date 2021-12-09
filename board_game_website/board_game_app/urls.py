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
    path('BoardGames/<int:boardgame_id>/', views.boardgame, name='boardgame'),
    #Page for adding a new board game
    path('new_boardgame/', views.new_boardgame, name='new_boardgame'),
]