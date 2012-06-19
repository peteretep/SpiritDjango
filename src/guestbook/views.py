from django.http import HttpResponse
from django.http import HttpResponseRedirect
from guestbook.models import Review
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from guestbook.models import ReviewForm

def index(request):
    review = Review.objects.all()
    t = loader.get_template('reviews.html')
    c = RequestContext({'review':review,
    })
    return HttpResponse(t.render(c))

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            entry = form.cleaned_data['entry']
            email = form.cleaned_data['email']
            new_review=form.save()
            new_review.name=name
            new_review.email=email
            new_review.entry=entry
            new_review.save()
            return HttpResponseRedirect('/')
    else:
        form = ReviewForm()
        
    return render_to_response('reviews.html', {'form': form},
                              context_instance=RequestContext(request))


