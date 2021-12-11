from django.shortcuts import render

from .models import BG

def index(request):
    #Home page
    return render(request, 'board_game_app/index.html')

def bgs_h(request):
    #BoardGames
    bgs_h = BG.objects.order_by('date_added')
    context = {'bgs_h': bgs_h}
    return render(request, 'board_game_app/bgs_h.html', context)

def bg(request, bg_id):
    #show a single bg and all its entries
    bg = BG.objects.get(id=bg_id)
    entries = bg.entry_set.order_by('-date_added')
    context = {'bg': bg, 'entries': entries}
    return render(request, 'board_game_app/bg.html', context)
# Create your views here.
