# Create your views here.
from django.http import HttpResponse
from home.models import Home
from home.models import Tours
from django.template import Context, loader



def index(request):
    home_textblock_list=Home.objects.all()
    t = loader.get_template('index.html')
    c = Context({'home_textblock_list':home_textblock_list,
    })
    return HttpResponse(t.render(c))

def tours(request):
    tours_textblock_list=Tours.objects.all()
    t= loader.get_template('tours.html')
    c = Context({'tours_textblock_list':tours_textblock_list,
    })
    return HttpResponse(t.render(c))
    