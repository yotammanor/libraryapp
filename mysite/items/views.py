from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Site

def index(request):
    latest_site_list = Site.objects.order_by('-pub_date')[:5]
    template = loader.get_template('items/index.html')
    context = RequestContext(request, {
        'latest_site_list': latest_site_list,
    })
    return HttpResponse(template.render(context))

def detail(request, site_id):
    return HttpResponse("You're looking at site %s." %site_id)

def results(request, site_id):
    return HttpResponse(response % site_id)

def comment(request, site_id):
    return HttpResponse("You're commenting site %s." %site_id)
