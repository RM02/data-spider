from django.urls import path
from front import views

urlpatterns = [
    path('index/', views.home)

]
