from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404, HttpResponseRedirect

from .forms import ShortenerForm
from .models import Shortener


def home_view(request):
    
    template = 'urlreduce/home.html'

    context = {}

    #Empty form
    context['form'] = ShortenerForm()

    if request.method ==  'GET':
        return render(request, template, context)

    elif request.method == 'POST':

        used_form = ShortenerForm(request.POST)
        test_url = request.POST.get('long_url')

        if used_form.is_valid():

            try:
                shortened_object = Shortener.objects.get(long_url=test_url)
                context['times_followed'] = shortened_object.times_followed

            except:
                shortened_object = used_form.save()

            new_url = request.build_absolute_uri('/') + shortened_object.short_url

            long_url = shortened_object.long_url

            context['new_url'] = new_url
            context['long_url'] = long_url

            return render(request, template, context)
        
        context['errors'] = used_form.errors
        
        return render(request, template, context)

def redirect_url_view(request, shortened_url):

    try:
        shortener = Shortener.objects.get(short_url=shortened_url)
        shortener.times_followed += 1
        shortener.save()

        return HttpResponseRedirect(shortener.long_url)

    except:
        raise Http404('Ouch! This link is broken')
        # return render(request, '404.html', status=404)
