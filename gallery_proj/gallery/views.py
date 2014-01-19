from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.shortcuts import render

# Create your views here.
def index(request):
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))