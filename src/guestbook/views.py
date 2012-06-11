from django.http import HttpResponse
from guestbook.models import Review
from django.template import Context, loader

def index(request):
    review_list = Review.objects.all()
    t = loader.get_template('index.html')
    c = Context({'review_list':review_list,
    })
    return HttpResponse(t.render(c))