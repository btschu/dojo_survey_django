from django.shortcuts import render, redirect

def form(request):
    return render(request,"form.html")

def process(request):
    name = request.POST['name']
    dojo_location = request.POST['dojo_location']
    favorite_language = request.POST['favorite_language']
    comments = request.POST['comments']
    context = {
    	"name" : name,
    	"dojo_location" : dojo_location,
    	"favorite_language" : favorite_language,
    	"comments" : comments,
    }
    print(request.POST)
    return render(request,"results.html", context)