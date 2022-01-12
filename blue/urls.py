from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name= 'index'),
    path('home.html',views.index, name= 'index'),
    path('about1.html',views.about1,name='about1'),
    path('training.html',views.training,name='training'),
    path('form1.html',views.form1,name='form1'),
    path('jobs.html',views.jobs,name='jobs'),
    path('success.html',views.success,name='success')
]