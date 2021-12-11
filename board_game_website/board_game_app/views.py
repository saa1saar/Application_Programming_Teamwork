from django.shortcuts import render

<<<<<<< HEAD
from .models import Topic

<<<<<<< HEAD
=======
>>>>>>> parent of 0c7026b (views.py Topics)
def index(request):
    #Home page
    return render(request, 'board_game_app/index.html')
=======
def BoarGames(request):
    #BoardGames
    BoardGames = BoardGame.objects.order_by('date_added')
    context = {'BoardGames': BoardGames}
    #Home page
    return render(request, 'board_game_app/BoardGame.html', context)
>>>>>>> parent of 5c4dd30 (views.py Boardgame)
# Create your views here.
