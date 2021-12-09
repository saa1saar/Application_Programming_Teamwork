from django.shortcuts import render

def index(request):
    #Home page
    return render(request, 'board_game_app/index.html')
# Create your views here.
