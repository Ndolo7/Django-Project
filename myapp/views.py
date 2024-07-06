from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

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
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our services are timely and quality is priority.  You will never regret working with us'
    feature1.is_true = True

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Top Quality Products'
    feature2.details = 'When it comes to quaily, you don\'t have to gamble. I provide my best skills.'
    feature2.is_true = True

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Always Available'
    feature3.details = 'Customer support cannot be compromised. I provide full support throughout the project'
    feature3.is_true = False

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Support Services'
    feature4.details = 'I offer support services like API integration, website hosting, database management,.. etc.'
    feature4.is_true = True
    
    features = [feature1, feature2, feature3, feature4]

    return render(request, 'index.html', {'features': features})

def counter(request):
    text = request.GET['text']
    word_count = len(text.split())
    return render(request, 'counter.html', {'count': word_count})