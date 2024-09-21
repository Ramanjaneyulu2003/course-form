from django.urls import path
from . import views
urlpatterns=[
    path('index',views.index),
    path('course',views.courseform),
    path('display',views.display),
    path('',views.dashboard,name='dashborad'),
    path('delete/<rid>',views.delete,name="delete")
] 
