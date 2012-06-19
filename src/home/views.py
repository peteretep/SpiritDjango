# Create your views here.
from django.http import HttpResponse
from home.models import Home
from home.models import Tours
from home.models import Angling
from home.models import Book
from home.models import Wildlife
from guestbook.models import Review
from django.template import Context, loader

import random


def index(request):
    okrevs = Review.objects.filter(checked = True)
    review=random.choice(okrevs)        
    textblock_list=Home.objects.all()
    t = loader.get_template('index.html')
    c = Context({'textblock_list':textblock_list, 'review':review
    })
    return HttpResponse(t.render(c))

def tours(request):
    okrevs = Review.objects.filter(checked = True)
    review=random.choice(okrevs)
    textblock_list=Tours.objects.all()
    t = loader.get_template('index.html')
    c = Context({'textblock_list':textblock_list, 'review':review
    })
    return HttpResponse(t.render(c))

def angling(request):
    okrevs = Review.objects.filter(checked = True)
    review=random.choice(okrevs)
    textblock_list=Angling.objects.all()
    t = loader.get_template('index.html')
    c = Context({'textblock_list':textblock_list, 'review':review
    })
    return HttpResponse(t.render(c))

def wildlife(request):
    okrevs = Review.objects.filter(checked = True)
    review=random.choice(okrevs)
    textblock_list=Wildlife.objects.all()
    t = loader.get_template('index.html')
    c = Context({'textblock_list':textblock_list, 'review':review
    })
    return HttpResponse(t.render(c))
    
def book(request):
    okrevs = Review.objects.filter(checked = True)
    review=random.choice(okrevs)
    textblock_list=Book.objects.all()
    t = loader.get_template('index.html')
    c = Context({'textblock_list':textblock_list, 'review':review
    })
    return HttpResponse(t.render(c))