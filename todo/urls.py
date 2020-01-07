from django.urls import path
from .views import Todolist,Tododetail, Todocreate,Tododelete ,Todoupdate

urlpatterns = [
    path('list/', Todolist.as_view() ,name='list'),
    path('detail/<int:pk>', Tododetail.as_view(),name='detail'),
    path('create/',Todocreate.as_view(),name='create'),
    path('delete/<int:pk>',Tododelete.as_view(),name='delete'),
    path('update/<int:pk>',Todoupdate.as_view(),name='update')
]
