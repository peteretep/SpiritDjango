# Create your views here.
from django.http import HttpResponse
from home.models import Home
from home.models import Tours
from home.models import Angling
from home.models import Book
from home.models import Wildlife
from guestbook.models import Review
from django.template import Context, loader


def index(request):
    reviews=Review.objects.all()

    textblock_list=Home.objects.all()
    t = loader.get_template('index.html')
    c = Context({'textblock_list':textblock_list, 'reviews':reviews
    })
    return HttpResponse(t.render(c))

def tours(request):
    reviews=Review.objects.all()
    textblock_list=Tours.objects.all()
    t = loader.get_template('index.html')
    c = Context({'textblock_list':textblock_list, 'reviews':reviews
    })
    return HttpResponse(t.render(c))

def angling(request):
    reviews=Review.objects.all()
    textblock_list=Angling.objects.all()
    t = loader.get_template('index.html')
    c = Context({'textblock_list':textblock_list, 'reviews':reviews
    })
    return HttpResponse(t.render(c))

def wildlife(request):
    reviews=Review.objects.all()
    textblock_list=Wildlife.objects.all()
    t = loader.get_template('index.html')
    c = Context({'textblock_list':textblock_list, 'reviews':reviews
    })
    return HttpResponse(t.render(c))
    
def book(request):
    reviews=Review.objects.all()
    textblock_list=Book.objects.all()
    t = loader.get_template('index.html')
    c = Context({'textblock_list':textblock_list, 'reviews':reviews
    })
    return HttpResponse(t.render(c))