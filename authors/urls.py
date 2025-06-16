from django.urls import path
from authors import views

app_name = 'recipes'

urlpatterns = [
    path('register/', views.register, name='register'),
]
