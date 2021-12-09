from django.shortcuts import render

from .models import Topic

def index(request):
    #Topics
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    #Home page
    return render(request, 'board_game_app/index.html')
# Create your views here.
