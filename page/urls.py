from django.urls import path
from page import views


urlpatterns = [
    path('', views.direct, name='direct'),
    path('index/', views.index, name='index'),
]