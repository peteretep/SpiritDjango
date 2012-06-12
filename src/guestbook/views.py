from django.http import HttpResponse
from guestbook.models import Review
from django.template import Context, loader


def index(request):
    review = Review.objects.all()
    t = loader.get_template('reviews.html')
    c = Context({'review':review,
    })
    return HttpResponse(t.render(c))