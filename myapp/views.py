from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
''' def index(request):  
 return HttpResponse('<h1> Welcome Onboard</h1>')
    context = {
        'name': 'patrick', or name = user.name (from database)
        'age': '23',
        'nationality': 'Kenyan',
    }
  return render(request, 'index.html', context)
 '''

def index(request):
    return render(request, 'index.html')

def counter(request):
    text = request.GET['text']
    word_count = len(text.split())
    return render(request, 'counter.html', {'count': word_count})