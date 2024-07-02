from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name ='index'), #Root url(main site)
    #path('/download', views.index, name ='index') download site
    path('counter', views.counter, name='counter')
]
   
   