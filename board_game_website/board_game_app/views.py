from django.shortcuts import redirect, render

from .models import BoardGame
from .forms import BoardGameForm, ReviewGameForm
from .forms import ReviewGameForm

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
    ReviewGame = boardgame.reviewgame_set.order_by('-date_added')
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

def new_review(request, boardgame_id):
    #add a review to an boardgame
    boardgame = BoardGame.objects.get(id=boardgame_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ReviewGameForm()
    else:
        # POST data submitted; process data.
        form = ReviewGameForm(data=request.POST)
        if form.is_valid():
           new_review = form.save(commit=False)
           new_review.boardgame = boardgame
           new_review.save()
           return redirect('board_game_app:boardgame', boardgame_id=boardgame_id)
    # Display a blank or invalid form.
    context = {'boardgame': boardgame, 'form': form}
    return render(request, 'board_game_app/new_review.html', context)

# Create your views here.
