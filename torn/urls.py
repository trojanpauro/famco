from django.urls import path

from . import views

urlpatterns = [
  path('myussd/',views.post,name='myussd')
]