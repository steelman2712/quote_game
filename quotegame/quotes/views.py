from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote
from random import choice
from django.contrib.auth.decorators import login_required

def random_quote():
    pks = Quote.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_obj = Quote.objects.get(pk=random_pk)
    return(random_obj)

# Create your views here.
@login_required
def index(request):
    quote = random_quote()
    resp = f"{quote.quote_text} - {quote.person}"
    return HttpResponse(resp)

@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })