from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import *
# Create your views here.
def hello(request):
    if request.user.is_authenticated():
        orderlist = Order.objects.filter(user_id = request.user.id)
        return render_to_response('home/home.html', {'user': request.user.username,'orderlist': orderlist})
    else:
        return HttpResponseRedirect('/accounts/login/')


def createOrder(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    
 
 
def createRoom(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    
    
    
    
    
    
    
    
    
    
    