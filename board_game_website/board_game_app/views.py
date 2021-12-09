from django.shortcuts import render, redirect

from .models import BoardGame
from .forms import BoardGameForm

def BoardGames(request):
    #BoardGames
    BoardGames = BoardGame.objects.order_by('date_added')
    context = {'BoardGames': BoardGames}
    #Home page
    return render(request, 'board_game_app/BoardGame.html', context)

def boardgame(request, boardgame_id):
    #boardgame = topic
    boardgame = BoardGame.objects.get(id=boardgame_id)
    #available games = entries
    availablegames = boardgame.entry_set.order_by('-date_added')
    context = {'boardgame': boardgame,'available games': availablegames}
    return render(request, 'board_game_app/BoardGames.html', context)

def new_boardgame(request): #Page523
    """Add a new boardgame."""
    if request.method !='POST':
        #No data submitted; create a blank form.
        form = BoardGameForm()
    else:
        # POST data submitted; process data.
        form = BoardGameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_game_app:BoardGames')

    # Display a blank or invalid form.
    context = {'form': form}
    returrn render(request,'board_game_app/new_boardgame.html', context)

# Create your views here.
