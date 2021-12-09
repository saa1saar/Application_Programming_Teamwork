from django.shortcuts import render

from .models import BoardGame

def BoardGames(request):
    #BoardGames
    BoardGames = BoardGame.objects.order_by('date_added')
    context = {'BoardGames': BoardGames}
    #Home page
    return render(request, 'board_game_app/BoardGame.html', context)

def boardgame(request, boardgame_id)
    #boardgame = topic
    boardgame = BoardGame.objects.get(id=topic_id)
    #available games = entries
    available games = topic.entry_set.order_by('-date_added')
    context = {'boardgame': boardgame,'available games': available games}
    return render(request, 'board_game_app/BoardGames.html', context)
# Create your views here.
