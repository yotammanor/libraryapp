from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from .models import Site

def index(request):
    latest_site_list = Site.objects.order_by('-pub_date')[:5]
    context = {'latest_site_list': latest_site_list}
    return render(request, 'items/index.html', context)

def details(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    return render(request,'items/details.html', {'site': site})

def results(request, site_id):
    return HttpResponse(response % site_id)

def comment(request, site_id):
    return HttpResponse("You're commenting site %s." %site_id)
