from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from quote.models import Quote
from quote.forms import QuoteForm
from django.db.models import Max
from django.db.models import Min
import random

import logging
logger = logging.getLogger(__name__)

def index(request):
    if "random" in request.path:
        quote = Quote.get_rand()
    else:
        quote = Quote.get_rand(daily=True)
    
    return render(request, 'quotes/quote.html', {'quote': quote})

def json(request):
    if "random" in request.path:
        quote = Quote.get_rand()
    else:
        quote = Quote.get_rand(daily=True)
        
    data = {
        'quote': quote.quote,
        'body': quote.body,
        'source': quote.source,
    }
    return JsonResponse(data)

def stats(request):
    total_count = Quote.objects.all().count()
    latest = Quote.objects.filter().latest('date_added')
    data = {
        'total': total_count,
        'latest': latest.quote,
    }
    return JsonResponse(data)

def add(request):
    if request.method == 'GET':
        form = QuoteForm()
        return render(request, 'quotes/add_quote.html', {'form':form})
        
    elif request.method == 'POST':
        data = request.POST
        print(data)
        form = QuoteForm(data)
        if form.is_valid():
            form.save()
            new_form = QuoteForm()
            return render(request, 'quotes/add_quote.html', {'form':new_form, 'success': True, 'data':data})

def authors(request,author_name=None):
    if author_name != None:
        author_quotes = Quote.objects.filter(source=author_name)
        return render(request, 'quotes/authors.html', {'author_quotes':author_quotes})
    else:
        authors = Quote.objects.order_by("source").values_list('source').distinct()
        return render(request, 'quotes/authors.html', {'authors':authors})

def json_authors(request):
        authors = Quote.objects.order_by("source").values_list('source').distinct()
        return JsonResponse(list(authors), safe=False)