from django.shortcuts import render

from .models import BoardGame

def index(request):
    return render(request, 'board_game_app/index.html')

def BoardGames(request):
    #BoardGames
    BoardGames = BoardGame.objects.order_by('date_added')
    context = {'BoardGames': BoardGames}
    #Home page
    return render(request, 'board_game_app/BoardGame.html', context)

def boardgame(request, boardgame_id):
    #boardgame = topic
    boardgame = BoardGame.objects.get(id=boardgame_id)
    #reviewgame = entries
    ReviewGame = boardgame.entry_set.order_by('-date_added')
    context = {'boardgame': boardgame,'review game': ReviewGame}
    return render(request, 'board_game_app/BoardGames.html', context)

def new_boardgame(request):
    #used for adding new games
    if request.method != 'POST':
        #incase there is no data -> create blank
        form = BoardGameForm()
    else:
        # create a new entry with the data
        form = BoardGameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_game_app:BoardGames')

    context = {'form': form}
    return render(request, 'board_game_app/new_boardgame.html', context)

# Create your views here.
